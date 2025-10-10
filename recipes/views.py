from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Recipe, Comment, Notification
from .forms import RecipeForm, CommentForm

def home(request):
    """Home page showing featured recipes and site overview"""
    # Get 4 random recipes for featured section
    featured_recipes = Recipe.objects.order_by('?')[:4]  # Random order
    
    context = {
        'total_users': User.objects.count(),
        'featured_recipes': featured_recipes,
        'total_recipes': Recipe.objects.count(),
    }
    return render(request, 'recipes/home.html', context)

class RecipeListView(ListView):
    """
    Enhanced recipe list view with integrated search and filtering
    """
    model = Recipe
    template_name = 'recipes/all_recipes.html'
    context_object_name = 'recipes'
    paginate_by = 9  # Show 9 recipes per page
    
    def get_queryset(self):
        """Apply search and filtering to the queryset"""
        queryset = Recipe.objects.all()
        
        # Get search parameters from URL
        query = self.request.GET.get('q', '').strip()
        category = self.request.GET.get('category', '').strip()
        max_prep_time = self.request.GET.get('max_prep_time', '').strip()
        max_cook_time = self.request.GET.get('max_cook_time', '').strip()
        sort_by = self.request.GET.get('sort', 'newest').strip()
        
        # Apply text search filter
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(ingredients__icontains=query) |
                Q(instructions__icontains=query)
            )
        
        # Apply meal type filter
        if category and category != 'all':
            queryset = queryset.filter(meal_type=category)
        
        # Apply tags filter (single selection)
        tag = self.request.GET.get('tags', '').strip()
        if tag:
            queryset = queryset.filter(recipe_tags__icontains=tag)
        
        # Apply prep time filter
        if max_prep_time:
            try:
                prep_time_int = int(max_prep_time)
                queryset = queryset.filter(prep_time__lte=prep_time_int)
            except ValueError:
                pass
        
        # Apply cook time filter
        if max_cook_time:
            try:
                cook_time_int = int(max_cook_time)
                queryset = queryset.filter(cook_time__lte=cook_time_int)
            except ValueError:
                pass
        
        # Apply sorting
        if sort_by == 'alphabetical':
            queryset = queryset.order_by('title')
        elif sort_by == 'prep_time':
            queryset = queryset.order_by('prep_time')
        elif sort_by == 'cook_time':
            queryset = queryset.order_by('cook_time')
        else:  # newest (default)
            queryset = queryset.order_by('-created_at')
        
        return queryset
    
    def get_context_data(self, **kwargs):
        """Add extra context data for search form and results"""
        context = super().get_context_data(**kwargs)
        
        # Get current search parameters
        context['current_query'] = self.request.GET.get('q', '')
        context['current_category'] = self.request.GET.get('category', '')
        context['current_tag'] = self.request.GET.get('tags', '')
        context['current_max_prep_time'] = self.request.GET.get('max_prep_time', '')
        context['current_max_cook_time'] = self.request.GET.get('max_cook_time', '')
        context['current_sort'] = self.request.GET.get('sort', 'newest')
        
        # Add choices for the filter dropdowns
        context['category_choices'] = Recipe.MEAL_TYPE_CHOICES
        context['recipe_tag_choices'] = Recipe.RECIPE_TAG_CHOICES
        context['tags_by_type'] = Recipe.get_tags_by_type()
        
        # Calculate total results
        context['total_recipes'] = self.get_queryset().count()
        context['total_all_recipes'] = Recipe.objects.count()
        
        # Check if any filters are active
        context['has_filters'] = any([
            context['current_query'],
            context['current_category'],
            context['current_tag'],
            context['current_max_prep_time'],
            context['current_max_cook_time'],
        ])
        
        return context


def index(request):
    if request.method == 'POST':
        return HttpResponse("You must have POSTed something")
    else:
        return HttpResponse(request.method)

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            messages.success(request, 'Recipe and image submitted successfully!')
            return redirect('recipe_detail', recipe.id)
        else:
            if 'image' in form.errors:
                messages.error(request, form.errors['image'][0])
            else:
                messages.error(request, 'Please correct the errors below.')
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})

def recipe_detail(request, recipe_id):
    """Display recipe details with comments"""
    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    # Get approved comments (newest first by default)
    comments = recipe.comments.filter(approved=True).order_by('-created_on')
    comments_count = comments.count()
    
    # Handle comment submission
    comment_submitted = False
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.success(request, 'Your comment has been submitted for approval!')
            comment_submitted = True
            # Redirect to prevent double submission
            return redirect('recipe_detail', recipe_id=recipe_id)
    else:
        comment_form = CommentForm()

    # Split ingredients into list
    ingredients_list = recipe.ingredients.split('\n') if recipe.ingredients else []

    context = {
        'recipe': recipe,
        'comments': comments,
        'comments_count': comments_count,
        'comment_form': comment_form,
        'comment_submitted': comment_submitted,
        'ingredients_list': ingredients_list,
    }
    
    return render(request, 'recipes/recipe_detail.html', context)


@login_required
def comment_edit(request, recipe_id, comment_id):
    """
    Edit a comment. Shows form on GET, updates on POST.
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)
    comment = get_object_or_404(Comment, pk=comment_id, recipe=recipe)

    if comment.author != request.user:
        messages.error(request, 'You can only edit your own comments!')
        return redirect('recipe_detail', recipe_id=recipe_id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            # Don't reset approval status for edits - keep existing approval state
            comment.save()
            messages.success(request, 'Comment updated!')
            return redirect('recipe_detail', recipe_id=recipe_id)
        else:
            messages.error(request, 'Error updating comment!')
    else:
        form = CommentForm(instance=comment)

    return render(request, 'recipes/edit_comment.html', {
        'form': form,
        'recipe': recipe,
        'comment': comment,
    })


@login_required
def comment_delete(request, recipe_id, comment_id):
    """
    Delete a comment.
    """
    comment = get_object_or_404(Comment, pk=comment_id, recipe_id=recipe_id)
    if comment.author == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')
    return redirect('recipe_detail', recipe_id=recipe_id)

@login_required
def recipe_edit(request, recipe_id):
    """
    Edit a recipe - only by the recipe author
    
    This view handles both GET requests (show the edit form) and 
    POST requests (process the form submission)
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    # Security check: only the author can edit their recipe
    if recipe.author != request.user:
        messages.error(request, 'You can only edit your own recipes!')
        return redirect('recipe_detail', recipe_id=recipe_id)
    
    if request.method == 'POST':
        # User submitted the edit form
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, f'Recipe "{recipe.title}" updated successfully!')
            return redirect('recipe_detail', recipe_id=recipe_id)
        else:
            if 'image' in form.errors:
                messages.error(request, form.errors['image'][0])
            else:
                messages.error(request, 'Please correct the errors below.')
    else:
        # User wants to see the edit form (GET request)
        form = RecipeForm(instance=recipe)
    
    return render(request, 'recipes/edit_recipe.html', {
        'form': form,
        'recipe': recipe,
    })

@login_required
def recipe_delete(request, recipe_id):
    """
    Delete a recipe - only by the recipe author
    
    This view only handles POST requests from the confirmation modal
    """
    # Get the recipe or return 404 if it doesn't exist
    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    # Security check: only the author can delete their recipe
    if recipe.author != request.user:
        messages.error(request, 'You can only delete your own recipes!')
        return redirect('recipe_detail', recipe_id=recipe_id)
    
    if request.method == 'POST':
        # User confirmed deletion from the modal
        recipe_title = recipe.title  # Store title before deletion
        recipe.delete()  # This also deletes all related comments (CASCADE)
        messages.success(request, f'Recipe "{recipe_title}" has been deleted successfully!')
        return redirect('recipes_home')
    
    # If someone tries to access this via GET, redirect back to detail page
    return redirect('recipe_detail', recipe_id=recipe_id)

def recipe_search(request):
    """Enhanced recipe search with multiple filters"""
    query = request.GET.get('q', '').strip()
    category = request.GET.get('category', '').strip()
    max_prep_time = request.GET.get('max_prep_time', '')
    max_cook_time = request.GET.get('max_cook_time', '')
    
    # Start with all recipes
    recipes = Recipe.objects.all()
    
    # Apply text search filter
    if query:
        recipes = recipes.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(ingredients__icontains=query) |
            Q(instructions__icontains=query) |
            Q(get_category_display_name__icontains=query)
        )
    
    # Apply category filter
    if category:
        recipes = recipes.filter(category=category)
    
    # Apply prep time filter
    if max_prep_time:
        try:
            prep_time_int = int(max_prep_time)
            recipes = recipes.filter(prep_time__lte=prep_time_int)
        except ValueError:
            pass
    
    # Apply cook time filter
    if max_cook_time:
        try:
            cook_time_int = int(max_cook_time)
            recipes = recipes.filter(cook_time__lte=cook_time_int)
        except ValueError:
            pass
    
    # Order results by relevance (newest first for now)
    recipes = recipes.order_by('-created_at')
    
    # Pagination
    paginator = Paginator(recipes, 9)  # 9 recipes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Prepare context
    context = {
        'recipes': page_obj,
        'query': query,
        'category': category,
        'max_prep_time': max_prep_time,
        'max_cook_time': max_cook_time,
        'total_results': recipes.count(),
        'category_choices': Recipe.CATEGORY_CHOICES,
        'categories_by_type': Recipe.get_categories_by_type(),
    }
    
    return render(request, 'recipes/search_results.html', context)


def recipes_by_category(request, category_slug):
    """Display all recipes in a specific category"""
    # Find the category from the choices
    category_name = None
    category_key = None
    
    for key, name in Recipe.CATEGORY_CHOICES:
        if key == category_slug:
            category_name = name
            category_key = key
            break
    
    if not category_name:
        raise Http404("Category not found")
    
    # Get recipes in this category
    recipes = Recipe.objects.filter(category=category_key).order_by('-created_at')
    
    # Pagination
    paginator = Paginator(recipes, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'recipes': page_obj,
        'category_name': category_name,
        'category_key': category_key,
        'total_recipes': recipes.count(),
    }
    
    return render(request, 'recipes/category_recipes.html', context)


def categories_list(request):
    """Display all available categories with recipe counts"""
    categories_data = []
    
    for category_key, category_name in Recipe.CATEGORY_CHOICES:
        recipe_count = Recipe.objects.filter(category=category_key).count()
        if recipe_count > 0:  # Only show categories that have recipes
            categories_data.append({
                'key': category_key,
                'name': category_name,
                'count': recipe_count,
            })
    
    # Group categories by type for better display
    categories_by_type = Recipe.get_categories_by_type()
    organized_categories = {}
    
    for type_name, type_categories in categories_by_type.items():
        organized_categories[type_name] = []
        for category_key, category_name in type_categories:
            recipe_count = Recipe.objects.filter(category=category_key).count()
            if recipe_count > 0:
                organized_categories[type_name].append({
                    'key': category_key,
                    'name': category_name,
                    'count': recipe_count,
                })
    
    context = {
        'categories_data': categories_data,
        'organized_categories': organized_categories,
        'total_categories': len(categories_data),
    }
    
    return render(request, 'recipes/categories_list.html', context)