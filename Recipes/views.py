from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.urls import reverse
from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm

def home(request):
    """Home page showing featured recipes and site overview"""
    # Get 4 random recipes for featured section
    featured_recipes = Recipe.objects.all().order_by('?')[:4]  # Random order, limit 4
    
    # Get totals for stats
    total_recipes = Recipe.objects.count()
    total_users = User.objects.count()
    
    context = {
        'featured_recipes': featured_recipes,
        'total_recipes': total_recipes,
        'total_users': total_users,
    }
    return render(request, 'recipes/home.html', context)

class RecipeListView(ListView):
    """
    Display all recipes with pagination
    Class-based view that automatically handles pagination
    """
    model = Recipe
    template_name = 'recipes/all_recipes.html'
    context_object_name = 'recipes'
    paginate_by = 6  # Show 6 recipes per page
    ordering = ['-created_at']  # Show newest first
    
    def get_context_data(self, **kwargs):
        """Add extra context data to the template"""
        context = super().get_context_data(**kwargs)
        context['total_recipes'] = Recipe.objects.count()
        return context


def index(request):
    if request.method == 'POST':
        return HttpResponse("You must have POSTed something")
    else:
        return HttpResponse(request.method)

@login_required
def add_recipe(request):
    """View for adding a new recipe - requires user authentication"""
    if request.method == 'POST':
        # Process form submission
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user  # Set the logged-in user as author
            recipe.save()
            messages.success(request, 'Recipe added successfully!')
            return redirect('home')  # Redirect to home page for now
    else:
        # Display empty form for GET request
        form = RecipeForm()
    
    return render(request, 'recipes/add_recipe.html', {'form': form})

def recipe_detail(request, recipe_id):
    """
    Display detailed view of a single recipe with comment functionality
    GET: Display recipe and approved comments
    POST: Handle comment submission (logged-in users only)
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    # Get approved comments only, ordered by newest first
    comments = recipe.comments.filter(approved=True).order_by('-created_on')
    
    # Handle comment form submission
    comment_form = CommentForm()
    comment_submitted = False
    
    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.author = request.user
            comment.save()
            
            messages.success(
                request,
                'Your comment has been submitted and is awaiting approval.'
            )
            comment_submitted = True
            # Create a new blank form after successful submission
            comment_form = CommentForm()
    
    # Split ingredients and instructions into lists for display
    ingredients_list = []
    if recipe.ingredients:
        ingredients_list = recipe.ingredients.split('\n')
    
    instructions_list = []
    if recipe.instructions:
        instructions_list = recipe.instructions.split('\n')
    
    context = {
        'recipe': recipe,
        'ingredients_list': ingredients_list,
        'instructions_list': instructions_list,
        'comments': comments,
        'comment_form': comment_form,
        'comment_submitted': comment_submitted,
        'comments_count': comments.count(),
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
    # Get the recipe or return 404 if it doesn't exist
    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    # Security check: only the author can edit their recipe
    if recipe.author != request.user:
        messages.error(request, 'You can only edit your own recipes!')
        return redirect('recipe_detail', recipe_id=recipe_id)
    
    if request.method == 'POST':
        # User submitted the edit form
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, f'Recipe "{recipe.title}" updated successfully!')
            return redirect('recipe_detail', recipe_id=recipe_id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        # User wants to see the edit form (GET request)
        form = RecipeForm(instance=recipe)
    
    return render(request, 'recipes/edit_recipe.html', {
        'form': form,
        'recipe': recipe
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