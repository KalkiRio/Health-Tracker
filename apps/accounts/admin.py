from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from .models import User, UserHealthProfile


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Enhanced User admin with medical profile fields"""
    
    list_display = [
        'username', 'email', 'first_name', 'last_name', 
        'blood_group', 'get_age_display', 'get_bmi_display', 'is_active'
    ]
    list_filter = [
        'is_active', 'is_staff', 'blood_group', 'activity_level',
        'date_joined', 'last_login'
    ]
    search_fields = ['username', 'email', 'first_name', 'last_name', 'phone_number']
    ordering = ['-date_joined']
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'phone_number', 
                      'date_of_birth', 'profile_picture')
        }),
        ('Physical Information', {
            'fields': ('height', 'current_weight', 'activity_level')
        }),
        ('Medical Information', {
            'fields': ('blood_group', 'known_allergies', 'medical_conditions', 
                      'current_medications'),
            'classes': ('collapse',)
        }),
        ('Emergency Contact', {
            'fields': ('emergency_contact_name', 'emergency_contact_relationship',
                      'emergency_contact_phone', 'emergency_contact_email'),
            'classes': ('collapse',)
        }),
        ('Healthcare Information', {
            'fields': ('insurance_provider', 'insurance_policy_number',
                      'preferred_hospital', 'primary_doctor_name', 'primary_doctor_phone'),
            'classes': ('collapse',)
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
            'classes': ('collapse',)
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    
    def get_age_display(self, obj):
        age = obj.get_age()
        return f"{age} years" if age else "Not specified"
    get_age_display.short_description = "Age"
    
    def get_bmi_display(self, obj):
        bmi = obj.get_bmi()
        if bmi:
            category = obj.get_bmi_category()
            color = {
                'Underweight': '#17a2b8',
                'Normal weight': '#28a745',
                'Overweight': '#ffc107',
                'Obese': '#dc3545'
            }.get(category, '#6c757d')
            return format_html(
                '<span style="color: {};">{} ({})</span>',
                color, bmi, category
            )
        return "Not calculated"
    get_bmi_display.short_description = "BMI"


@admin.register(UserHealthProfile)
class UserHealthProfileAdmin(admin.ModelAdmin):
    """Admin for User Health Profiles"""
    
    list_display = [
        'user', 'primary_goal', 'target_weight', 'daily_calorie_target',
        'medication_reminders', 'updated_at'
    ]
    list_filter = ['primary_goal', 'medication_reminders', 'share_data_with_doctor']
    search_fields = ['user__username', 'user__email', 'user__first_name', 'user__last_name']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('User', {'fields': ('user',)}),
        ('Health Goals', {
            'fields': ('primary_goal', 'target_weight', 'daily_calorie_target', 
                      'daily_water_target', 'target_steps_per_day', 
                      'target_exercise_minutes_per_week')
        }),
        ('Notifications', {
            'fields': ('medication_reminders', 'appointment_reminders', 
                      'health_tips', 'weekly_reports')
        }),
        ('Privacy', {
            'fields': ('share_data_with_doctor', 'allow_health_insights')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )