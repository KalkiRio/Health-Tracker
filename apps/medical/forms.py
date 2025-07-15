
from django import forms
from .models import MedicalReport, Appointment

class MedicalReportForm(forms.ModelForm):
    class Meta:
        model = MedicalReport
        fields = ['title', 'report_type', 'file', 'description', 'doctor_name', 'clinic_hospital', 'report_date']
        widgets = {
            'report_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Additional notes about this report...'}),
            'title': forms.TextInput(attrs={'placeholder': 'e.g., Blood Test Results'}),
            'doctor_name': forms.TextInput(attrs={'placeholder': 'Doctor\'s name'}),
            'clinic_hospital': forms.TextInput(attrs={'placeholder': 'Clinic or hospital name'}),
        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor_name', 'clinic_hospital', 'appointment_date', 'duration_minutes', 'reason', 'notes']
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'doctor_name': forms.TextInput(attrs={'placeholder': 'Doctor\'s name'}),
            'clinic_hospital': forms.TextInput(attrs={'placeholder': 'Clinic or hospital name'}),
            'reason': forms.TextInput(attrs={'placeholder': 'Reason for visit'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Additional notes...'}),
            'duration_minutes': forms.NumberInput(attrs={'value': 30}),
        }
