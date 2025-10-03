from django.contrib import admin
from .models import Recipe, Comment


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


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin interface for managing comments with approval functionality"""
    
    list_display = [
        'recipe',
        'author',
        'body_preview',
        'created_on',
        'approved'
    ]
    list_filter = ['approved', 'created_on', 'recipe']
    search_fields = ['body', 'author__username', 'recipe__title']
    readonly_fields = ['created_on']
    actions = ['approve_comments', 'disapprove_comments']
    
    # Order by newest first
    ordering = ['-created_on']
    
    def body_preview(self, obj):
        """Show first 50 characters of comment body"""
        return obj.body[:50] + '...' if len(obj.body) > 50 else obj.body
    body_preview.short_description = 'Comment Preview'
    
    def approve_comments(self, request, queryset):
        """Bulk action to approve selected comments"""
        updated = queryset.update(approved=True)
        self.message_user(
            request,
            f'{updated} comment(s) were successfully approved.'
        )
    approve_comments.short_description = 'Approve selected comments'
    
    def disapprove_comments(self, request, queryset):
        """Bulk action to disapprove selected comments"""
        updated = queryset.update(approved=False)
        self.message_user(
            request,
            f'{updated} comment(s) were disapproved.'
        )
    disapprove_comments.short_description = 'Disapprove selected comments'
