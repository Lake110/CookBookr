from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        'title', 
        'author', 
        'prep_time', 
        'cook_time', 
        'servings', 
        'created_at'
    ]
    list_filter = ['created_at', 'author', 'prep_time', 'cook_time']
    search_fields = ['title', 'ingredients', 'description']
    readonly_fields = ['created_at', 'updated_at']
    
    # Organize the admin form into sections
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'author')
        }),
        ('Recipe Details', {
            'fields': ('ingredients', 'instructions', 'servings')
        }),
        ('Timing', {
            'fields': ('prep_time', 'cook_time')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
