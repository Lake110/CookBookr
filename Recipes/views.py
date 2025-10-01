from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User  
from django.views.generic import ListView
from .models import Recipe
from .forms import RecipeForm

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


def recipe_home(request):
    """Legacy function view - redirects to class-based view"""
    from django.shortcuts import redirect
    return redirect('recipes_list')

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