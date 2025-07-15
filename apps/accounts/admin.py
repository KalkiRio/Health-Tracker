from django.contrib import admin
from .models import UserProfile, MedicalProfile, UserHealthProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'date_of_birth', 'gender']
    search_fields = ['user__username', 'user__email', 'phone_number']
    list_filter = ['gender', 'blood_group']