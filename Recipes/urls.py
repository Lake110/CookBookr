from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_home, name='recipes_home'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
]