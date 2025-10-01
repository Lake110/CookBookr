from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title', 
            'description', 
            'ingredients', 
            'instructions', 
            'prep_time', 
            'cook_time', 
            'servings'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter recipe title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Brief description of your recipe'
            }),
            'ingredients': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'List ingredients (one per line)'
            }),
            'instructions': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 8,
                'placeholder': 'Step-by-step cooking instructions'
            }),
            'prep_time': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Prep time in minutes'
            }),
            'cook_time': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cook time in minutes'
            }),
            'servings': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number of servings'
            })
        }

