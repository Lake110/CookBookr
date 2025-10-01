from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipes_home'),
    path('list/', views.RecipeListView.as_view(), name='recipes_list'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
]