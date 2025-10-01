from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    ingredients = models.TextField(
        help_text="List ingredients, one per line"
    )
    instructions = models.TextField(
        help_text="Step-by-step cooking instructions"
    )
    prep_time = models.IntegerField(
        help_text="Preparation time in minutes"
    )
    cook_time = models.IntegerField(help_text="Cooking time in minutes")
    servings = models.IntegerField(default=1)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipes'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_total_time(self):
        return self.prep_time + self.cook_time


class Comment(models.Model):
    """Comment model for recipe reviews and feedback"""
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    body = models.TextField(
        max_length=1000,
        help_text="Share your thoughts about this recipe"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Comment by {self.author.username} on {self.recipe.title}'
