from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from .models import Recipe, Comment


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


class CommentForm(forms.ModelForm):
    """Form for users to submit comments on recipes"""
    
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Share your thoughts about this recipe...'
            })
        }
        labels = {
            'body': 'Your Comment'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('body', css_class='form-control'),
            Submit('submit', 'Post Comment', css_class='btn btn-primary mt-2')
        )
        self.helper.form_method = 'post'

