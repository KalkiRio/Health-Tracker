from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'profile_picture', 'date_of_birth', 'gender', 'height', 'blood_group',
            'activity_level', 'phone_number', 'address', 'emergency_contact_name',
            'emergency_contact_phone', 'emergency_contact_relationship', 'allergies',
            'chronic_conditions', 'current_medications', 'insurance_provider',
            'insurance_policy_number', 'preferred_hospital', 'preferred_doctor'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 3}),
            'allergies': forms.Textarea(attrs={'rows': 3}),
            'chronic_conditions': forms.Textarea(attrs={'rows': 3}),
            'current_medications': forms.Textarea(attrs={'rows': 3}),
        }