
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class WeightEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='weight_entries')
    weight = models.FloatField(validators=[MinValueValidator(0.1), MaxValueValidator(1000)])
    date_recorded = models.DateField(default=timezone.now)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_recorded']
        unique_together = ['user', 'date_recorded']
    
    def __str__(self):
        return f"{self.user.username} - {self.weight}kg on {self.date_recorded}"

class VitalSigns(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vital_signs')
    systolic_bp = models.IntegerField(validators=[MinValueValidator(50), MaxValueValidator(300)], null=True, blank=True)
    diastolic_bp = models.IntegerField(validators=[MinValueValidator(30), MaxValueValidator(200)], null=True, blank=True)
    heart_rate = models.IntegerField(validators=[MinValueValidator(30), MaxValueValidator(220)], null=True, blank=True)
    blood_glucose = models.FloatField(validators=[MinValueValidator(20), MaxValueValidator(600)], null=True, blank=True)
    temperature = models.FloatField(validators=[MinValueValidator(90), MaxValueValidator(110)], null=True, blank=True)
    date_recorded = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-date_recorded']
    
    def __str__(self):
        return f"{self.user.username} - Vitals on {self.date_recorded.date()}"

class Exercise(models.Model):
    EXERCISE_TYPES = [
        ('cardio', 'Cardio'),
        ('strength', 'Strength Training'),
        ('flexibility', 'Flexibility'),
        ('sports', 'Sports'),
        ('walking', 'Walking'),
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
        ('yoga', 'Yoga'),
        ('other', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exercises')
    exercise_type = models.CharField(max_length=20, choices=EXERCISE_TYPES)
    name = models.CharField(max_length=100)
    duration_minutes = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1440)])
    calories_burned = models.IntegerField(validators=[MinValueValidator(0)], null=True, blank=True)
    date_performed = models.DateField(default=timezone.now)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_performed']
    
    def __str__(self):
        return f"{self.user.username} - {self.name} on {self.date_performed}"

class Meal(models.Model):
    MEAL_TYPES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals')
    name = models.CharField(max_length=200)
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPES)
    calories = models.IntegerField(validators=[MinValueValidator(0)], null=True, blank=True)
    date_consumed = models.DateField(default=timezone.now)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_consumed']
    
    def __str__(self):
        return f"{self.user.username} - {self.name} ({self.meal_type})"

class HealthGoal(models.Model):
    GOAL_TYPES = [
        ('weight_loss', 'Weight Loss'),
        ('weight_gain', 'Weight Gain'),
        ('muscle_gain', 'Muscle Gain'),
        ('fitness', 'General Fitness'),
        ('blood_pressure', 'Blood Pressure Control'),
        ('blood_glucose', 'Blood Glucose Control'),
        ('exercise', 'Exercise Goal'),
        ('other', 'Other'),
    ]
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('paused', 'Paused'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='health_goals')
    goal_type = models.CharField(max_length=20, choices=GOAL_TYPES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    target_value = models.FloatField()
    current_value = models.FloatField(default=0)
    unit = models.CharField(max_length=20)
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
