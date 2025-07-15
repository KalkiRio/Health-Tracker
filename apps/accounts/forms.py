from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, MedicalProfile, UserHealthProfile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'date_of_birth', 'gender', 'height', 'activity_level', 'profile_picture']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'height': forms.NumberInput(attrs={'step': '0.1', 'placeholder': 'Height in cm'}),
        }

class MedicalProfileForm(forms.ModelForm):
    class Meta:
        model = MedicalProfile
        fields = [
            'blood_group', 'allergies', 'medical_conditions', 'current_medications',
            'emergency_contact_name', 'emergency_contact_phone', 'emergency_contact_relation',
            'insurance_provider', 'policy_number', 'primary_doctor', 'doctor_phone',
            'preferred_hospital'
        ]
        widgets = {
            'allergies': forms.Textarea(attrs={'rows': 3}),
            'medical_conditions': forms.Textarea(attrs={'rows': 3}),
            'current_medications': forms.Textarea(attrs={'rows': 3}),
        }

class UserHealthProfileForm(forms.ModelForm):
    class Meta:
        model = UserHealthProfile
        fields = [
            'primary_goal', 'target_weight', 'daily_calorie_target', 'daily_water_target',
            'target_steps_per_day', 'target_exercise_minutes_per_week',
            'medication_reminders', 'appointment_reminders', 'health_tips', 'weekly_reports',
            'share_data_with_doctor', 'allow_health_insights'
        ]
        widgets = {
            'target_weight': forms.NumberInput(attrs={'step': '0.1'}),
            'daily_water_target': forms.NumberInput(attrs={'step': '0.5'}),
        }