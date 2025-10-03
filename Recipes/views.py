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
    # Make sure you're getting recipes with images
    featured_recipes = Recipe.objects.all()[:4]  # Get first 4 recipes

    context = {
        'total_users': User.objects.count(),
        'featured_recipes': featured_recipes,  # Add this line
        'total_recipes': Recipe.objects.count(),
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
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_detail', recipe.id)
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
    # Get the recipe or return 404 if it doesn't exist
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