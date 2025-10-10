from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Recipe(models.Model):
    # Primary meal type choices
    MEAL_TYPE_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'), 
        ('dinner', 'Dinner'),
        ('snacks', 'Snacks & Appetizers'),
        ('dessert', 'Desserts'),
        ('beverages', 'Beverages'),
    ]
    
    # Recipe tag choices for multiple selection
    RECIPE_TAG_CHOICES = [
        # Cuisine Types
        ('italian', 'Italian'),
        ('mexican', 'Mexican'),
        ('asian', 'Asian'),
        ('chinese', 'Chinese'),
        ('indian', 'Indian'),
        ('american', 'American'),
        ('mediterranean', 'Mediterranean'),
        ('french', 'French'),
        ('thai', 'Thai'),
        ('japanese', 'Japanese'),
        
        # Dietary Preferences
        ('vegetarian', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('gluten_free', 'Gluten-Free'),
        ('dairy_free', 'Dairy-Free'),
        ('keto', 'Keto/Low-Carb'),
        ('paleo', 'Paleo'),
        ('healthy', 'Healthy & Light'),
        ('low_sodium', 'Low Sodium'),
        
        # Cooking Methods
        ('grilled', 'Grilled'),
        ('baked', 'Baked'),
        ('fried', 'Fried'),
        ('steamed', 'Steamed'),
        ('slow_cooked', 'Slow Cooked'),
        ('no_cook', 'No Cooking Required'),
        
        # Dish Types
        ('soup', 'Soup'),
        ('salad', 'Salad'),
        ('pasta', 'Pasta'),
        ('pizza', 'Pizza'),
        ('burger', 'Burger'),
        ('sandwich', 'Sandwich'),
        ('casserole', 'Casserole'),
        ('stir_fry', 'Stir Fry'),
        
        # Protein Types
        ('chicken', 'Chicken'),
        ('beef', 'Beef'),
        ('pork', 'Pork'),
        ('seafood', 'Seafood'),
        ('fish', 'Fish'),
        ('lamb', 'Lamb'),
        ('turkey', 'Turkey'),
        
        # Cooking Time/Difficulty
        ('quick', 'Quick (Under 30 min)'),
        ('easy', 'Easy to Make'),
        ('budget_friendly', 'Budget-Friendly'),
        ('one_pot', 'One Pot/Pan'),
        ('meal_prep', 'Meal Prep Friendly'),
        ('comfort_food', 'Comfort Food'),
        ('spicy', 'Spicy'),
        ('kid_friendly', 'Kid-Friendly'),
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
    
    # Primary meal type (single selection)
    meal_type = models.CharField(
        max_length=50,
        choices=MEAL_TYPE_CHOICES,
        default='dinner',
        help_text="Select the primary meal type for this recipe"
    )
    
    # Recipe tags (multiple selection stored as comma-separated string)
    recipe_tags = models.CharField(
        max_length=500,
        blank=True,
        help_text="Multiple tags describing this recipe (cuisine, dietary, etc.)"
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
    
    def get_meal_type_display_name(self):
        """Return the human-readable meal type name"""
        return dict(self.MEAL_TYPE_CHOICES).get(self.meal_type, self.meal_type)
    
    def get_recipe_tags_list(self):
        """Return recipe tags as a list"""
        if self.recipe_tags:
            return [tag.strip() for tag in self.recipe_tags.split(',')]
        return []
    
    def get_recipe_tags_display(self):
        """Return formatted recipe tags for display"""
        tags = self.get_recipe_tags_list()
        tag_dict = dict(self.RECIPE_TAG_CHOICES)
        return [tag_dict.get(tag, tag) for tag in tags]
    
    def set_recipe_tags(self, tag_list):
        """Set recipe tags from a list"""
        if tag_list:
            self.recipe_tags = ','.join(tag_list)
        else:
            self.recipe_tags = ''
    
    @classmethod
    def get_tags_by_type(cls):
        """Return recipe tags organized by type for better UI"""
        return {
            'Cuisine': [
                ('italian', 'Italian'),
                ('mexican', 'Mexican'),
                ('asian', 'Asian'),
                ('chinese', 'Chinese'),
                ('indian', 'Indian'),
                ('american', 'American'),
                ('mediterranean', 'Mediterranean'),
                ('french', 'French'),
                ('thai', 'Thai'),
                ('japanese', 'Japanese'),
            ],
            'Dietary': [
                ('vegetarian', 'Vegetarian'),
                ('vegan', 'Vegan'),
                ('gluten_free', 'Gluten-Free'),
                ('dairy_free', 'Dairy-Free'),
                ('keto', 'Keto/Low-Carb'),
                ('paleo', 'Paleo'),
                ('healthy', 'Healthy & Light'),
                ('low_sodium', 'Low Sodium'),
            ],
            'Cooking Methods': [
                ('grilled', 'Grilled'),
                ('baked', 'Baked'),
                ('fried', 'Fried'),
                ('steamed', 'Steamed'),
                ('slow_cooked', 'Slow Cooked'),
                ('no_cook', 'No Cooking Required'),
            ],
            'Dish Types': [
                ('soup', 'Soup'),
                ('salad', 'Salad'),
                ('pasta', 'Pasta'),
                ('pizza', 'Pizza'),
                ('burger', 'Burger'),
                ('sandwich', 'Sandwich'),
                ('casserole', 'Casserole'),
                ('stir_fry', 'Stir Fry'),
            ],
            'Protein': [
                ('chicken', 'Chicken'),
                ('beef', 'Beef'),
                ('pork', 'Pork'),
                ('seafood', 'Seafood'),
                ('fish', 'Fish'),
                ('lamb', 'Lamb'),
                ('turkey', 'Turkey'),
            ],
            'Features': [
                ('quick', 'Quick (Under 30 min)'),
                ('easy', 'Easy to Make'),
                ('budget_friendly', 'Budget-Friendly'),
                ('one_pot', 'One Pot/Pan'),
                ('meal_prep', 'Meal Prep Friendly'),
                ('comfort_food', 'Comfort Food'),
                ('spicy', 'Spicy'),
                ('kid_friendly', 'Kid-Friendly'),
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

