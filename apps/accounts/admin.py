from django.contrib import admin
from .models import UserProfile, MedicalProfile, UserHealthProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'date_of_birth', 'gender', 'height', 'activity_level']
    list_filter = ['gender', 'activity_level']
    search_fields = ['user__username', 'user__email', 'phone']

@admin.register(MedicalProfile)
class MedicalProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'blood_group', 'emergency_contact_name', 'primary_doctor']
    list_filter = ['blood_group']
    search_fields = ['user__username', 'emergency_contact_name', 'primary_doctor']

@admin.register(UserHealthProfile)
class UserHealthProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'primary_goal', 'target_weight', 'daily_calorie_target']
    list_filter = ['primary_goal']
    search_fields = ['user__username']