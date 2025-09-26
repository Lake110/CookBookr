from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Recipe App!")

def recipe_home(request):
    return HttpResponse("Welcome to the Recipes page")

def index(request):
    if request.method == 'POST':
        return HttpResponse("You must have POSTed something")
    else:
        return HttpResponse(request.method)