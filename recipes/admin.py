from django.contrib import admin
from .models import Recipe, Comment


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Enhanced admin interface for Recipe model"""
    list_display = [
        'title', 
        'get_category_display_name', 
        'author', 
        'prep_time', 
        'cook_time', 
        'servings',
        'created_at'
    ]
    list_filter = [
        'category', 
        'author', 
        'created_at',
        'prep_time',
        'cook_time'
    ]
    search_fields = [
        'title', 
        'description', 
        'ingredients', 
        'author__username'
    ]
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'image', 'category')
        }),
        ('Recipe Details', {
            'fields': ('ingredients', 'instructions', 'prep_time', 'cook_time', 'servings')
        }),
        ('Metadata', {
            'fields': ('author', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin interface for Comment model"""
    list_display = [
        'recipe', 
        'author', 
        'body_preview', 
        'created_on', 
        'approved'
    ]
    list_filter = [
        'approved', 
        'created_on', 
        'recipe'
    ]
    search_fields = [
        'body', 
        'author__username', 
        'recipe__title'
    ]
    actions = ['approve_comments']

    def body_preview(self, obj):
        """Show first 50 characters of comment body"""
        return obj.body[:50] + "..." if len(obj.body) > 50 else obj.body
    body_preview.short_description = 'Comment Preview'

    def approve_comments(self, request, queryset):
        """Bulk approve comments"""
        queryset.update(approved=True)
    approve_comments.short_description = "Approve selected comments"
