
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class WeightEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='weight_entries')
    weight = models.FloatField(help_text="Weight in kg")
    date_recorded = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_recorded']
        verbose_name_plural = "Weight Entries"
    
    def __str__(self):
        return f"{self.user.username} - {self.weight}kg on {self.date_recorded.date()}"

class VitalSigns(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vital_signs')
    systolic_bp = models.IntegerField(null=True, blank=True, help_text="Systolic blood pressure")
    diastolic_bp = models.IntegerField(null=True, blank=True, help_text="Diastolic blood pressure")
    heart_rate = models.IntegerField(null=True, blank=True, help_text="Heart rate (bpm)")
    blood_glucose = models.FloatField(null=True, blank=True, help_text="Blood glucose (mg/dL)")
    temperature = models.FloatField(null=True, blank=True, help_text="Body temperature (°C)")
    date_recorded = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_recorded']
        verbose_name_plural = "Vital Signs"
    
    def __str__(self):
        return f"{self.user.username} - Vitals on {self.date_recorded.date()}"

class Exercise(models.Model):
    EXERCISE_TYPES = [
        ('cardio', 'Cardio'),
        ('strength', 'Strength Training'),
        ('flexibility', 'Flexibility/Yoga'),
        ('sports', 'Sports'),
        ('walking', 'Walking'),
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
        ('other', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exercises')
    exercise_type = models.CharField(max_length=20, choices=EXERCISE_TYPES)
    exercise_name = models.CharField(max_length=100)
    duration_minutes = models.IntegerField(help_text="Duration in minutes")
    calories_burned = models.IntegerField(null=True, blank=True)
    date_performed = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_performed']
    
    def __str__(self):
        return f"{self.user.username} - {self.exercise_name} ({self.duration_minutes}min)"

class Meal(models.Model):
    MEAL_TYPES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals')
    meal_name = models.CharField(max_length=100)
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPES)
    calories = models.IntegerField(help_text="Estimated calories")
    protein = models.FloatField(null=True, blank=True, help_text="Protein in grams")
    carbs = models.FloatField(null=True, blank=True, help_text="Carbohydrates in grams")
    fat = models.FloatField(null=True, blank=True, help_text="Fat in grams")
    date_consumed = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_consumed']
    
    def __str__(self):
        return f"{self.user.username} - {self.meal_name} ({self.meal_type})"

class HealthGoal(models.Model):
    GOAL_TYPES = [
        ('weight_loss', 'Weight Loss'),
        ('weight_gain', 'Weight Gain'),
        ('muscle_gain', 'Muscle Gain'),
        ('fitness', 'Fitness Improvement'),
        ('endurance', 'Endurance'),
        ('strength', 'Strength'),
        ('health', 'General Health'),
    ]
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('paused', 'Paused'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='health_goals')
    goal_type = models.CharField(max_length=20, choices=GOAL_TYPES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    target_value = models.FloatField(help_text="Target value (weight, time, etc.)")
    current_value = models.FloatField(default=0)
    unit = models.CharField(max_length=20, help_text="kg, minutes, etc.")
    target_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.title}"
    
    @property
    def progress_percentage(self):
        if self.target_value == 0:
            return 0
        return min((self.current_value / self.target_value) * 100, 100)
