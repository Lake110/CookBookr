from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from .models import Recipe, Comment


class RecipeForm(forms.ModelForm):
    """Enhanced form for creating and editing recipes with organized category selection"""
    
    # Custom field for single tag selection
    recipe_tags = forms.ChoiceField(
        choices=[('', 'Select a tag (optional)')] + Recipe.RECIPE_TAG_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        required=False,
        label='Recipe Tags'
    )
    
    class Meta:
        model = Recipe
        fields = [
            'title', 
            'description', 
            'image', 
            'meal_type',
            'recipe_tags',
            'ingredients', 
            'instructions', 
            'prep_time', 
            'cook_time', 
            'servings'
        ]
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter recipe title...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Brief description of your recipe...'
            }),
            'meal_type': forms.Select(attrs={
                'class': 'form-select'
            }),
            'ingredients': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'List ingredients, one per line:\n• 2 cups flour\n• 1 tsp salt\n• 3 eggs'
            }),
            'instructions': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 8,
                'placeholder': 'Step-by-step instructions:\n1. Preheat oven to 350°F\n2. Mix dry ingredients...'
            }),
            'prep_time': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'placeholder': 'Minutes'
            }),
            'cook_time': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'placeholder': 'Minutes'
            }),
            'servings': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'max': '50',
                'placeholder': 'Number of servings'
            }),
        }
        
        labels = {
            'prep_time': 'Preparation Time (minutes)',
            'cook_time': 'Cooking Time (minutes)',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # If editing an existing recipe, populate the selected tag (first one only)
        if self.instance and self.instance.pk:
            selected_tags = self.instance.get_recipe_tags_list()
            if selected_tags:
                self.fields['recipe_tags'].initial = selected_tags[0]
        
        # Make certain fields required with custom error messages
        self.fields['title'].required = True
        self.fields['ingredients'].required = True
        self.fields['instructions'].required = True
        self.fields['meal_type'].required = True
    
    def clean_title(self):
        """Validate recipe title"""
        title = self.cleaned_data.get('title')
        if title:
            title = title.strip()
            if len(title) < 3:
                raise forms.ValidationError("Recipe title must be at least 3 characters long.")
        return title
    
    def clean_prep_time(self):
        """Validate preparation time"""
        prep_time = self.cleaned_data.get('prep_time')
        if prep_time is not None and prep_time < 0:
            raise forms.ValidationError("Preparation time cannot be negative.")
        return prep_time
    
    def clean_cook_time(self):
        """Validate cooking time"""
        cook_time = self.cleaned_data.get('cook_time')
        if cook_time is not None and cook_time < 0:
            raise forms.ValidationError("Cooking time cannot be negative.")
        return cook_time
    
    def clean(self):
        """Cross-field validation"""
        cleaned_data = super().clean()
        prep_time = cleaned_data.get('prep_time')
        cook_time = cleaned_data.get('cook_time')
        
        # Check if total time is reasonable
        if prep_time and cook_time:
            total_time = prep_time + cook_time
            if total_time > 600:  # 10 hours
                raise forms.ValidationError(
                    "Total cooking time seems unusually long. Please verify your times."
                )
        
        return cleaned_data
    
    def save(self, commit=True):
        """Custom save method to handle recipe tags"""
        recipe = super().save(commit=False)
        
        # Handle single recipe tag
        selected_tag = self.cleaned_data.get('recipe_tags', '')
        if selected_tag:
            recipe.set_recipe_tags([selected_tag])
        else:
            recipe.set_recipe_tags([])
        
        if commit:
            recipe.save()
        return recipe


class CommentForm(forms.ModelForm):
    """Form for adding comments to recipes"""
    
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Share your thoughts about this recipe, tips, or modifications you made...'
            })
        }
        labels = {
            'body': 'Your Comment'
        }
    
    def clean_body(self):
        """Validate comment content"""
        body = self.cleaned_data.get('body')
        if body:
            body = body.strip()
            if len(body) < 10:
                raise forms.ValidationError("Please write a more detailed comment (at least 10 characters).")
            if len(body) > 1000:
                raise forms.ValidationError("Comment is too long. Please keep it under 1000 characters.")
        return body


class RecipeSearchForm(forms.Form):
    """Advanced search form for recipes"""
    
    query = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search recipes, ingredients, or keywords...',
        }),
        label='Search'
    )
    
    meal_type = forms.ChoiceField(
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        label='Meal Type'
    )
    
    tags = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-check-input'
        }),
        label='Recipe Tags'
    )
    
    max_prep_time = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': '0',
            'placeholder': 'Max prep time (minutes)'
        }),
        label='Max Preparation Time'
    )
    
    max_cook_time = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': '0',
            'placeholder': 'Max cook time (minutes)'
        }),
        label='Max Cooking Time'
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Set up meal type choices for search
        meal_type_choices = [('', 'All Meal Types')]
        meal_type_choices.extend(Recipe.MEAL_TYPE_CHOICES)
        self.fields['meal_type'].choices = meal_type_choices
        
        # Set up tag choices for search
        self.fields['tags'].choices = Recipe.RECIPE_TAG_CHOICES

