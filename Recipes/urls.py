from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_home, name='recipes_home'),
    path('add/', views.add_recipe, name='add_recipe'),
]