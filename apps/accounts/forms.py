from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field, Div, HTML
from crispy_forms.bootstrap import FormActions
from .models import User, UserHealthProfile


class CustomUserCreationForm(UserCreationForm):
    """Custom user registration form"""
    
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text="Optional: Helps calculate age-appropriate health recommendations"
    )
    phone_number = forms.CharField(max_length=15, required=False)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'date_of_birth', 
                 'phone_number', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML('<h3 class="mb-4">Create Your HealthTracker Account</h3>'),
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-3'),
                Column('last_name', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            Row(
                Column('username', css_class='form-group col-md-6 mb-3'),
                Column('email', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            Row(
                Column('date_of_birth', css_class='form-group col-md-6 mb-3'),
                Column('phone_number', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            Row(
                Column('password1', css_class='form-group col-md-6 mb-3'),
                Column('password2', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            FormActions(
                Submit('submit', 'Create Account', css_class='btn btn-primary btn-lg w-100')
            )
        )
        
        # Add Bootstrap classes
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.date_of_birth = self.cleaned_data.get('date_of_birth')
        user.phone_number = self.cleaned_data.get('phone_number', '')
        
        if commit:
            user.save()
            # Create health profile
            UserHealthProfile.objects.create(user=user)
        return user


class UserProfileForm(forms.ModelForm):
    """Form for updating user profile information"""
    
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email', 'phone_number', 'date_of_birth',
            'profile_picture', 'height', 'current_weight', 'activity_level',
            'blood_group', 'known_allergies', 'medical_conditions', 'current_medications',
            'emergency_contact_name', 'emergency_contact_relationship', 
            'emergency_contact_phone', 'emergency_contact_email',
            'insurance_provider', 'insurance_policy_number',
            'preferred_hospital', 'primary_doctor_name', 'primary_doctor_phone'
        ]
        
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'known_allergies': forms.Textarea(attrs={'rows': 3}),
            'medical_conditions': forms.Textarea(attrs={'rows': 3}),
            'current_medications': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML('<h3 class="mb-4">Personal Information</h3>'),
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-3'),
                Column('last_name', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            Row(
                Column('email', css_class='form-group col-md-6 mb-3'),
                Column('phone_number', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            Row(
                Column('date_of_birth', css_class='form-group col-md-6 mb-3'),
                Column('profile_picture', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            
            HTML('<hr><h3 class="mb-4">Physical Information</h3>'),
            Row(
                Column('height', css_class='form-group col-md-4 mb-3'),
                Column('current_weight', css_class='form-group col-md-4 mb-3'),
                Column('activity_level', css_class='form-group col-md-4 mb-3'),
                css_class='form-row'
            ),
            
            HTML('<hr><h3 class="mb-4">Medical Information</h3>'),
            Row(
                Column('blood_group', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            Field('known_allergies'),
            Field('medical_conditions'),
            Field('current_medications'),
            
            HTML('<hr><h3 class="mb-4">Emergency Contact</h3>'),
            Row(
                Column('emergency_contact_name', css_class='form-group col-md-6 mb-3'),
                Column('emergency_contact_relationship', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            Row(
                Column('emergency_contact_phone', css_class='form-group col-md-6 mb-3'),
                Column('emergency_contact_email', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            
            HTML('<hr><h3 class="mb-4">Healthcare Information</h3>'),
            Row(
                Column('insurance_provider', css_class='form-group col-md-6 mb-3'),
                Column('insurance_policy_number', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            Row(
                Column('preferred_hospital', css_class='form-group col-md-12 mb-3'),
                css_class='form-row'
            ),
            Row(
                Column('primary_doctor_name', css_class='form-group col-md-6 mb-3'),
                Column('primary_doctor_phone', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            
            FormActions(
                Submit('submit', 'Update Profile', css_class='btn btn-primary btn-lg')
            )
        )
        
        # Add Bootstrap classes and help text
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            
            # Add specific help text
            if field_name == 'height':
                field.help_text = "Height in centimeters (e.g., 175)"
            elif field_name == 'current_weight':
                field.help_text = "Weight in kilograms (e.g., 70.5)"


class HealthProfileForm(forms.ModelForm):
    """Form for updating health profile settings"""
    
    class Meta:
        model = UserHealthProfile
        fields = [
            'primary_goal', 'target_weight', 'daily_calorie_target', 'daily_water_target',
            'target_steps_per_day', 'target_exercise_minutes_per_week',
            'medication_reminders', 'appointment_reminders', 'health_tips', 'weekly_reports',
            'share_data_with_doctor', 'allow_health_insights'
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML('<h3 class="mb-4">Health Goals</h3>'),
            Row(
                Column('primary_goal', css_class='form-group col-md-6 mb-3'),
                Column('target_weight', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            Row(
                Column('daily_calorie_target', css_class='form-group col-md-6 mb-3'),
                Column('daily_water_target', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            Row(
                Column('target_steps_per_day', css_class='form-group col-md-6 mb-3'),
                Column('target_exercise_minutes_per_week', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            
            HTML('<hr><h3 class="mb-4">Notification Preferences</h3>'),
            Row(
                Column('medication_reminders', css_class='form-group col-md-6 mb-3'),
                Column('appointment_reminders', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            Row(
                Column('health_tips', css_class='form-group col-md-6 mb-3'),
                Column('weekly_reports', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            
            HTML('<hr><h3 class="mb-4">Privacy Settings</h3>'),
            Row(
                Column('share_data_with_doctor', css_class='form-group col-md-6 mb-3'),
                Column('allow_health_insights', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            
            FormActions(
                Submit('submit', 'Update Health Profile', css_class='btn btn-success btn-lg')
            )
        )


class CustomLoginForm(forms.Form):
    """Custom login form with email or username"""
    
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username or Email',
            'autofocus': True
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )
    remember_me = forms.BooleanField(required=False)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML('<h3 class="mb-4 text-center">Welcome Back!</h3>'),
            Field('username'),
            Field('password'),
            Field('remember_me'),
            FormActions(
                Submit('submit', 'Sign In', css_class='btn btn-primary btn-lg w-100')
            )
        )
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if username and password:
            # Try to authenticate with username first, then email
            user = authenticate(username=username, password=password)
            if user is None:
                # Try with email
                try:
                    user_obj = User.objects.get(email=username)
                    user = authenticate(username=user_obj.username, password=password)
                except User.DoesNotExist:
                    pass
            
            if user is None:
                raise forms.ValidationError("Invalid username/email or password.")
            elif not user.is_active:
                raise forms.ValidationError("This account is inactive.")
        
        return self.cleaned_data