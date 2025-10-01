from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipes_home'),
    path('list/', views.RecipeListView.as_view(), name='recipes_list'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:recipe_id>/edit_comment/<int:comment_id>/',
         views.comment_edit, name='comment_edit'),
    path('recipe/<int:recipe_id>/delete_comment/<int:comment_id>/',
         views.comment_delete, name='comment_delete'),
]