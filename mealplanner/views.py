from django.shortcuts import render, redirect
from datetime import date, timedelta
from .models import MealPlan, MealSlot
from .forms import MealSlotForm
from recipes.models import Recipe
from django.http import JsonResponse
import json

def meal_planner(request):
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    meal_plan, _ = MealPlan.objects.get_or_create(user=request.user, week_start=week_start)

    slots = { (slot.day, slot.meal_type): slot for slot in meal_plan.slots.all() }
    today_index = today.weekday()
    context = {
        'week_days': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        'slots': slots,
        'meal_plan': meal_plan,
        'today_index': today_index,
        'all_recipes': Recipe.objects.all(),
    }
    return render(request, 'mealplanner/calendar.html', context)

def assign_recipe(request):
    data = json.loads(request.body)
    recipe = Recipe.objects.get(id=data['recipeId'])
    week_start = date.today() - timedelta(days=date.today().weekday())
    meal_plan = MealPlan.objects.get(user=request.user, week_start=week_start)
    slot, _ = MealSlot.objects.get_or_create(meal_plan=meal_plan, day=data['day'], meal_type=data['meal'])
    slot.recipe = recipe
    slot.save()
    return JsonResponse({'status': 'success'})

def add_recipe_to_slot(request):
    if request.method == 'POST':
        day = request.POST['day']
        meal_type = request.POST['meal_type']
        recipe_id = request.POST['recipe']
        recipe = Recipe.objects.get(id=recipe_id)

        MealSlot.objects.update_or_create(
            day=day,
            meal_type=meal_type,
            defaults={'recipe': recipe}
        )
        return redirect('meal_planner')

def meal_planner_view(request):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    meal_types = ['Breakfast', 'Lunch', 'Dinner', 'Snack']
    meal_slots = MealSlot.objects.select_related('recipe').all()
    all_recipes = Recipe.objects.all()

    return render(request, 'mealplanner/calendar.html', {
        'days': days,
        'meal_types': meal_types,
        'meal_slots': meal_slots,
        'all_recipes': all_recipes,
    })