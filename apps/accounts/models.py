from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class UserProfile(models.Model):
    """Extended user profile with basic information"""

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    ACTIVITY_CHOICES = [
        ('sedentary', 'Sedentary (little or no exercise)'),
        ('light', 'Light (exercise 1-3 times/week)'),
        ('moderate', 'Moderate (exercise 4-5 times/week)'),
        ('active', 'Active (daily exercise or intense exercise 3-4 times/week)'),
        ('extra', 'Extra Active (very intense exercise daily, or physical job)'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # Basic Information
    phone = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    height = models.FloatField(null=True, blank=True, help_text="Height in cm")
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    # Activity Level
    activity_level = models.CharField(max_length=20, choices=ACTIVITY_CHOICES, default='moderate')

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def get_absolute_url(self):
        return reverse('accounts:profile')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Resize image
        if self.profile_picture:
            img = Image.open(self.profile_picture.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.profile_picture.path)

class MedicalProfile(models.Model):
    """Medical profile information"""

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='medical_profile')

    # Medical Information
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, blank=True)
    allergies = models.TextField(blank=True, help_text="List any known allergies")
    medical_conditions = models.TextField(blank=True, help_text="Chronic conditions, past surgeries, etc.")
    current_medications = models.TextField(blank=True, help_text="Current medications and dosages")

    # Emergency Contact
    emergency_contact_name = models.CharField(max_length=100, blank=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True)
    emergency_contact_relation = models.CharField(max_length=50, blank=True)

    # Insurance Information
    insurance_provider = models.CharField(max_length=100, blank=True)
    policy_number = models.CharField(max_length=50, blank=True)

    # Doctor Information
    primary_doctor = models.CharField(max_length=100, blank=True)
    doctor_phone = models.CharField(max_length=15, blank=True)
    preferred_hospital = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Medical Profile"

class UserHealthProfile(models.Model):
    """Additional health profile information that can be updated frequently"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='health_profile')

    # Health Goals
    GOAL_CHOICES = [
        ('weight_loss', 'Weight Loss'),
        ('weight_gain', 'Weight Gain'),
        ('muscle_gain', 'Muscle Gain'),
        ('fitness', 'General Fitness'),
        ('health', 'Health Maintenance'),
        ('recovery', 'Recovery/Rehabilitation'),
    ]
    primary_goal = models.CharField(max_length=20, choices=GOAL_CHOICES, default='health')
    target_weight = models.FloatField(null=True, blank=True)
    daily_calorie_target = models.IntegerField(null=True, blank=True)
    daily_water_target = models.FloatField(default=8.0, help_text="Target water intake in glasses")

    # Health Metrics Targets
    target_steps_per_day = models.IntegerField(default=10000)
    target_exercise_minutes_per_week = models.IntegerField(default=150)

    # Notification Preferences
    medication_reminders = models.BooleanField(default=True)
    appointment_reminders = models.BooleanField(default=True)
    health_tips = models.BooleanField(default=True)
    weekly_reports = models.BooleanField(default=True)

    # Privacy Settings
    share_data_with_doctor = models.BooleanField(default=False)
    allow_health_insights = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Health Profile"