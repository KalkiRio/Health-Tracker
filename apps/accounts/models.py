from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

def get_profile_upload_path(instance, filename):
    return f'profile_pics/{instance.user.username}/{filename}'

class UserProfile(models.Model):
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O-',),
    ]

    ACTIVITY_LEVELS = [
        ('sedentary', 'Sedentary (little/no exercise)'),
        ('light', 'Light (light exercise 1-3 days/week)'),
        ('moderate', 'Moderate (moderate exercise 3-5 days/week)'),
        ('active', 'Active (hard exercise 6-7 days/week)'),
        ('very_active', 'Very Active (physical job + exercise)'),
    ]

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to=get_profile_upload_path, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    height = models.FloatField(help_text="Height in cm", null=True, blank=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, blank=True)
    activity_level = models.CharField(max_length=20, choices=ACTIVITY_LEVELS, default='moderate')
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True)
    emergency_contact_relationship = models.CharField(max_length=50, blank=True)
    allergies = models.TextField(blank=True, help_text="List any known allergies")
    chronic_conditions = models.TextField(blank=True, help_text="List any chronic medical conditions")
    current_medications = models.TextField(blank=True, help_text="List current medications")
    insurance_provider = models.CharField(max_length=100, blank=True)
    insurance_policy_number = models.CharField(max_length=50, blank=True)
    preferred_hospital = models.CharField(max_length=100, blank=True)
    preferred_doctor = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def get_absolute_url(self):
        return reverse('accounts:profile')

    @property
    def age(self):
        if self.date_of_birth:
            from datetime import date
            today = date.today()
            return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return None

    @property
    def current_weight(self):
        latest_weight = self.user.weight_entries.first()
        return latest_weight.weight if latest_weight else None

    @property
    def bmi(self):
        if self.height and self.current_weight:
            height_m = self.height / 100  # Convert cm to meters
            return round(self.current_weight / (height_m ** 2), 1)
        return None

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Resize profile picture if it exists
        if self.profile_picture:
            img = Image.open(self.profile_picture.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.profile_picture.path)

# Create profile automatically when user is created
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()