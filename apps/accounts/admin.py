
from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'date_of_birth', 'gender', 'blood_group']
    search_fields = ['user__username', 'user__email', 'phone_number']
    list_filter = ['gender', 'blood_group', 'activity_level']
    fieldsets = (
        ('Basic Information', {
            'fields': ('user', 'profile_picture', 'date_of_birth', 'gender', 'height')
        }),
        ('Contact Information', {
            'fields': ('phone_number', 'address')
        }),
        ('Medical Information', {
            'fields': ('blood_group', 'activity_level', 'allergies', 'chronic_conditions', 'current_medications')
        }),
        ('Emergency Contact', {
            'fields': ('emergency_contact_name', 'emergency_contact_phone', 'emergency_contact_relationship')
        }),
        ('Insurance & Healthcare', {
            'fields': ('insurance_provider', 'insurance_policy_number', 'preferred_hospital', 'preferred_doctor')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
