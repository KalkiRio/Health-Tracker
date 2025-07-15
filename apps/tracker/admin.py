
from django.contrib import admin
from .models import WeightEntry, VitalSigns, Exercise, Meal, HealthGoal

@admin.register(WeightEntry)
class WeightEntryAdmin(admin.ModelAdmin):
    list_display = ['user', 'weight', 'date_recorded']
    list_filter = ['date_recorded']
    search_fields = ['user__username']
    date_hierarchy = 'date_recorded'

@admin.register(VitalSigns)
class VitalSignsAdmin(admin.ModelAdmin):
    list_display = ['user', 'systolic_bp', 'diastolic_bp', 'heart_rate', 'date_recorded']
    list_filter = ['date_recorded']
    search_fields = ['user__username']
    date_hierarchy = 'date_recorded'

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['user', 'exercise_name', 'exercise_type', 'duration_minutes', 'date_performed']
    list_filter = ['exercise_type', 'date_performed']
    search_fields = ['user__username', 'exercise_name']
    date_hierarchy = 'date_performed'

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ['user', 'meal_name', 'meal_type', 'calories', 'date_consumed']
    list_filter = ['meal_type', 'date_consumed']
    search_fields = ['user__username', 'meal_name']
    date_hierarchy = 'date_consumed'

@admin.register(HealthGoal)
class HealthGoalAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'goal_type', 'target_value', 'current_value', 'status']
    list_filter = ['goal_type', 'status']
    search_fields = ['user__username', 'title']
