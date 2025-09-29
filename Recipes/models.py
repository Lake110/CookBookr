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
