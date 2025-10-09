from django import forms
from .models import MealSlot
from recipes.models import Recipe

class MealSlotForm(forms.ModelForm):
    class Meta:
        model = MealSlot
        fields = ['day', 'meal_type', 'recipe', 'notes']
        widgets = {
            'day': forms.Select(attrs={'class': 'form-select'}),
            'meal_type': forms.Select(attrs={'class': 'form-select'}),
            'recipe': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
