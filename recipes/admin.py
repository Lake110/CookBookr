from django.contrib import admin
from .models import Recipe, Comment


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Enhanced admin interface for Recipe model"""

    list_display = [
        "title",
        "get_meal_type_display_name",
        "get_tags_display_short",
        "author",
        "prep_time",
        "cook_time",
        "servings",
        "created_at",
    ]
    list_filter = [
        "meal_type",
        "author",
        "created_at",
        "prep_time",
        "cook_time",
    ]
    search_fields = [
        "title",
        "description",
        "ingredients",
        "recipe_tags",
        "author__username",
    ]
    ordering = ["-created_at"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        ("Basic Information", {"fields": ("title", "description", "image")}),
        ("Categories", {"fields": ("meal_type", "recipe_tags")}),
        (
            "Recipe Details",
            {
                "fields": (
                    "ingredients",
                    "instructions",
                    "prep_time",
                    "cook_time",
                    "servings",
                )
            },
        ),
        (
            "Metadata",
            {
                "fields": ("author", "created_at", "updated_at"),
                "classes": ("collapse",),
            },
        ),
    )

    def get_tags_display_short(self, obj):
        """Show first few tags for list display"""
        tags = obj.get_recipe_tags_display()
        if not tags:
            return "No tags"
        if len(tags) > 2:
            return f"{', '.join(tags[:2])} (+{len(tags)-2} more)"
        return ", ".join(tags)

    get_tags_display_short.short_description = "Tags"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin interface for Comment model"""

    list_display = [
        "recipe",
        "author",
        "body_preview",
        "created_on",
        "approved",
    ]
    list_filter = ["approved", "created_on", "recipe"]
    search_fields = [
        "body",
        "author__username",
        "recipe__title",
    ]
    actions = ["approve_comments"]

    def body_preview(self, obj):
        """Show first 50 characters of comment body"""
        return obj.body[:50] + "..." if len(obj.body) > 50 else obj.body

    body_preview.short_description = "Comment Preview"

    def approve_comments(self, request, queryset):
        """Bulk approve comments"""
        queryset.update(approved=True)

    approve_comments.short_description = "Approve selected comments"
