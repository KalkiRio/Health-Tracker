
from django import forms
from .models import Medicine, MedicationReminder, Prescription

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = [
            'name', 'dosage_form', 'strength', 'frequency', 'dosage_instructions',
            'prescribed_by', 'start_date', 'end_date', 'notes', 'prescription_image'
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'dosage_instructions': forms.Textarea(attrs={'rows': 3, 'placeholder': 'e.g., Take with food, before meals'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Additional notes about this medicine...'}),
            'name': forms.TextInput(attrs={'placeholder': 'Medicine name'}),
            'strength': forms.TextInput(attrs={'placeholder': 'e.g., 500mg, 5ml'}),
            'prescribed_by': forms.TextInput(attrs={'placeholder': 'Doctor\'s name'}),
        }

class MedicationReminderForm(forms.ModelForm):
    class Meta:
        model = MedicationReminder
        fields = ['time']
        widgets = {
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['doctor_name', 'clinic_hospital', 'prescription_date', 'image', 'notes']
        widgets = {
            'prescription_date': forms.DateInput(attrs={'type': 'date'}),
            'doctor_name': forms.TextInput(attrs={'placeholder': 'Doctor\'s name'}),
            'clinic_hospital': forms.TextInput(attrs={'placeholder': 'Clinic or hospital name'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Additional notes...'}),
        }
