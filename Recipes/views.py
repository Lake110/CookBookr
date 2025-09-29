from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Recipe

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