from django import template
from mealplanner.models import MealSlot

register = template.Library()

@register.filter
def get_slot(slots, day_meal):
    day, meal_type = day_meal.split('|')
    return slots.filter(day=day, meal_type=meal_type).first()

@register.simple_tag
def get_meal_slot(meal_slots, day, meal_type):
    return meal_slots.filter(day=day, meal_type=meal_type).first()
