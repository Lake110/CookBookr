from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Recipe
from .forms import RecipeForm

def home(request):
    # Show recent 6 recipes on homepage
    recent_recipes = Recipe.objects.all()[:6]
    return render(request, 'recipes/home.html', {'recipes': recent_recipes})

def recipe_home(request):
    # Show all recipes
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

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
    Display detailed view of a single recipe
    Available to all users (no login required)
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    # Potential Future additions: Track recipe views (for future analytics)
    # You could add a views counter field to the Recipe model later
    
    context = {
        'recipe': recipe,
        'ingredients_list': recipe.ingredients.split('\n') if recipe.ingredients else [],
        'instructions_list': recipe.instructions.split('\n') if recipe.instructions else [],
    }
    
    return render(request, 'recipes/recipe_detail.html', context)