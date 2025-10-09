from django.urls import path
from . import views

urlpatterns = [
    path('planner/', views.meal_planner, name='meal_planner'),
    path('assign/', views.assign_recipe, name='assign_recipe'),
    path('add-recipe/', views.add_recipe_to_slot, name='add_recipe_to_slot'),
]
