from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Recipe(models.Model):
    # Predefined category choices
    CATEGORY_CHOICES = [
        # Meal Types
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'), 
        ('dinner', 'Dinner'),
        ('snacks', 'Snacks & Appetizers'),
        ('dessert', 'Desserts'),
        ('beverages', 'Beverages'),
        
        # Cuisine Types
        ('italian', 'Italian'),
        ('mexican', 'Mexican'),
        ('asian', 'Asian'),
        ('indian', 'Indian'),
        ('american', 'American'),
        ('mediterranean', 'Mediterranean'),
        
        # Dietary & Specific
        ('vegetarian', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('gluten_free', 'Gluten-Free'),
        ('keto', 'Keto/Low-Carb'),
        ('healthy', 'Healthy & Light'),
        
        # Popular Dish Types
        ('pizza', 'Pizza'),
        ('burger', 'Burgers'),
        ('pasta', 'Pasta'),
        ('soup', 'Soups & Stews'),
        ('salad', 'Salads'),
        ('chicken', 'Chicken Dishes'),
        ('seafood', 'Seafood'),
        ('beef', 'Beef Dishes'),
        ('pork', 'Pork Dishes'),
        ('baking', 'Baking & Bread'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = CloudinaryField('image', default='placeholder')
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
    
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='dinner',
        help_text="Select the most appropriate category for this recipe"
    )
    
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
    
    def get_category_display_name(self):
        """Return the human-readable category name"""
        return dict(self.CATEGORY_CHOICES).get(self.category, self.category)
    
    @classmethod
    def get_categories_by_type(cls):
        """Return categories organized by type for better UI"""
        return {
            'Meal Types': [
                ('breakfast', 'Breakfast'),
                ('lunch', 'Lunch'),
                ('dinner', 'Dinner'),
                ('snacks', 'Snacks & Appetizers'),
                ('dessert', 'Desserts'),
                ('beverages', 'Beverages'),
            ],
            'Cuisine': [
                ('italian', 'Italian'),
                ('mexican', 'Mexican'),
                ('asian', 'Asian'),
                ('indian', 'Indian'),
                ('american', 'American'),
                ('mediterranean', 'Mediterranean'),
            ],
            'Dietary': [
                ('vegetarian', 'Vegetarian'),
                ('vegan', 'Vegan'),
                ('gluten_free', 'Gluten-Free'),
                ('keto', 'Keto/Low-Carb'),
                ('healthy', 'Healthy & Light'),
            ],
            'Popular Dishes': [
                ('pizza', 'Pizza'),
                ('burger', 'Burgers'),
                ('pasta', 'Pasta'),
                ('soup', 'Soups & Stews'),
                ('salad', 'Salads'),
                ('chicken', 'Chicken Dishes'),
                ('seafood', 'Seafood'),
                ('beef', 'Beef Dishes'),
                ('pork', 'Pork Dishes'),
                ('baking', 'Baking & Bread'),
            ]
        }


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
