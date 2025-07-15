
from django.contrib import admin
from .models import WeightEntry, Exercise, WaterIntake, SleepRecord, MoodEntry

@admin.register(WeightEntry)
class WeightEntryAdmin(admin.ModelAdmin):
    list_display = ['user', 'weight', 'date_recorded', 'created_at']
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

@admin.register(WaterIntake)
class WaterIntakeAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount_ml', 'date_recorded', 'created_at']
    list_filter = ['date_recorded']
    search_fields = ['user__username']
    date_hierarchy = 'date_recorded'
    ordering = ['-date_recorded']

@admin.register(SleepRecord)
class SleepRecordAdmin(admin.ModelAdmin):
    list_display = ['user', 'sleep_date', 'bedtime', 'wake_time', 'hours_slept', 'quality_rating']
    list_filter = ['sleep_date', 'quality_rating']
    search_fields = ['user__username']
    date_hierarchy = 'sleep_date'
    ordering = ['-sleep_date']

@admin.register(MoodEntry)
class MoodEntryAdmin(admin.ModelAdmin):
    list_display = ['user', 'mood_rating', 'energy_level', 'date_recorded']
    list_filter = ['mood_rating', 'energy_level', 'date_recorded']
    search_fields = ['user__username']
    date_hierarchy = 'date_recorded'
    ordering = ['-date_recorded']
