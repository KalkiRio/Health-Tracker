
from django.contrib import admin
from .models import WeightEntry, VitalSigns, Exercise, Meal, HealthGoal

@admin.register(WeightEntry)
class WeightEntryAdmin(admin.ModelAdmin):
    list_display = ['user', 'weight', 'date_recorded', 'created_at']
    list_filter = ['date_recorded']
    search_fields = ['user__username']
    date_hierarchy = 'date_recorded'
    ordering = ['-date_recorded']

@admin.register(VitalSigns)
class VitalSignsAdmin(admin.ModelAdmin):
    list_display = ['user', 'systolic_bp', 'diastolic_bp', 'heart_rate', 'blood_glucose', 'temperature', 'date_recorded']
    list_filter = ['date_recorded']
    search_fields = ['user__username']
    date_hierarchy = 'date_recorded'
    ordering = ['-date_recorded']

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'exercise_type', 'duration_minutes', 'calories_burned', 'date_performed']
    list_filter = ['exercise_type', 'date_performed']
    search_fields = ['user__username', 'name']
    date_hierarchy = 'date_performed'
    ordering = ['-date_performed']

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'meal_type', 'calories', 'date_consumed']
    list_filter = ['meal_type', 'date_consumed']
    search_fields = ['user__username', 'name']
    date_hierarchy = 'date_consumed'
    ordering = ['-date_consumed']

@admin.register(HealthGoal)
class HealthGoalAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'goal_type', 'target_value', 'current_value', 'status', 'target_date']
    list_filter = ['goal_type', 'status', 'target_date']
    search_fields = ['user__username', 'title']
    date_hierarchy = 'target_date'
    ordering = ['-created_at']
