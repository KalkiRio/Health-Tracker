from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image

class User(AbstractUser):
    """Extended User model with health and medical profile information"""
    
    # Basic Profile Information
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics/', 
        default='profile_pics/default.jpg',
        blank=True
    )
    
    # Physical Characteristics
    height = models.FloatField(
        null=True, 
        blank=True, 
        help_text="Height in centimeters",
        validators=[MinValueValidator(50), MaxValueValidator(300)]
    )
    current_weight = models.FloatField(
        null=True, 
        blank=True, 
        help_text="Current weight in kilograms",
        validators=[MinValueValidator(20), MaxValueValidator(500)]
    )
    
    # Activity Level
    ACTIVITY_CHOICES = [
        ('sedentary', 'Sedentary (little/no exercise)'),
        ('light', 'Lightly active (light exercise 1-3 days/week)'),
        ('moderate', 'Moderately active (moderate exercise 3-5 days/week)'),
        ('active', 'Very active (hard exercise 6-7 days/week)'),
        ('extra', 'Extra active (very hard exercise, physical job)')
    ]
    activity_level = models.CharField(
        max_length=20, 
        choices=ACTIVITY_CHOICES, 
        default='moderate'
    )
    
    # Medical Information
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A Positive'),
        ('A-', 'A Negative'),
        ('B+', 'B Positive'),
        ('B-', 'B Negative'),
        ('AB+', 'AB Positive'),
        ('AB-', 'AB Negative'),
        ('O+', 'O Positive'),
        ('O-', 'O Negative'),
        ('unknown', 'Unknown'),
    ]
    blood_group = models.CharField(
        max_length=10, 
        choices=BLOOD_GROUP_CHOICES, 
        default='unknown'
    )
    
    # Medical Conditions and Allergies
    known_allergies = models.TextField(
        blank=True,
        help_text="List any known allergies (food, medication, environmental)"
    )
    medical_conditions = models.TextField(
        blank=True,
        help_text="List any chronic conditions, diseases, or ongoing medical issues"
    )
    current_medications = models.TextField(
        blank=True,
        help_text="List current medications and dosages"
    )
    
    # Emergency Contact Information
    emergency_contact_name = models.CharField(max_length=100, blank=True)
    emergency_contact_relationship = models.CharField(max_length=50, blank=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True)
    emergency_contact_email = models.EmailField(blank=True)
    
    # Insurance Information
    insurance_provider = models.CharField(max_length=100, blank=True)
    insurance_policy_number = models.CharField(max_length=50, blank=True)
    
    # Healthcare Preferences
    preferred_hospital = models.CharField(max_length=200, blank=True)
    primary_doctor_name = models.CharField(max_length=100, blank=True)
    primary_doctor_phone = models.CharField(max_length=15, blank=True)
    
    # Privacy Settings
    profile_visibility = models.BooleanField(
        default=True,
        help_text="Make basic profile information visible to healthcare providers"
    )
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        db_table = 'accounts_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return f"{self.get_full_name()} ({self.email})"
    
    def get_full_name(self):
        """Return the user's full name or username if name is not available"""
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username
    
    def get_age(self):
        """Calculate and return user's age"""
        if self.date_of_birth:
            from datetime import date
            today = date.today()
            return today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
            )
        return None
    
    def get_bmi(self):
        """Calculate and return BMI if height and weight are available"""
        if self.height and self.current_weight:
            height_m = self.height / 100  # Convert cm to meters
            bmi = self.current_weight / (height_m ** 2)
            return round(bmi, 1)
        return None
    
    def get_bmi_category(self):
        """Return BMI category based on WHO standards"""
        bmi = self.get_bmi()
        if bmi is None:
            return "Unknown"
        elif bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"
    
    def save(self, *args, **kwargs):
        """Override save to resize profile pictures"""
        super().save(*args, **kwargs)
        
        if self.profile_picture:
            img = Image.open(self.profile_picture.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.profile_picture.path)


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
    
    class Meta:
        db_table = 'accounts_user_health_profile'
        verbose_name = 'User Health Profile'
        verbose_name_plural = 'User Health Profiles'
    
    def __str__(self):
        return f"{self.user.get_full_name()}'s Health Profile"