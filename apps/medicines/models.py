
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Medicine(models.Model):
    DOSAGE_FORMS = [
        ('tablet', 'Tablet'),
        ('capsule', 'Capsule'),
        ('syrup', 'Syrup'),
        ('injection', 'Injection'),
        ('drops', 'Drops'),
        ('cream', 'Cream/Ointment'),
        ('inhaler', 'Inhaler'),
        ('other', 'Other'),
    ]
    
    FREQUENCY_CHOICES = [
        ('once_daily', 'Once Daily'),
        ('twice_daily', 'Twice Daily'),
        ('three_times', 'Three Times Daily'),
        ('four_times', 'Four Times Daily'),
        ('weekly', 'Weekly'),
        ('as_needed', 'As Needed'),
        ('custom', 'Custom Schedule'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='medicines')
    name = models.CharField(max_length=100)
    dosage_form = models.CharField(max_length=20, choices=DOSAGE_FORMS)
    strength = models.CharField(max_length=50, help_text="e.g., 500mg, 5ml")
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES)
    dosage_instructions = models.TextField(help_text="e.g., Take with food, before meals")
    prescribed_by = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    notes = models.TextField(blank=True)
    prescription_image = models.ImageField(upload_to='prescriptions/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.strength} ({self.user.username})"

class MedicationReminder(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='reminders')
    time = models.TimeField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['time']
    
    def __str__(self):
        return f"{self.medicine.name} at {self.time}"

class MedicationLog(models.Model):
    STATUS_CHOICES = [
        ('taken', 'Taken'),
        ('missed', 'Missed'),
        ('skipped', 'Skipped'),
    ]
    
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='logs')
    scheduled_time = models.DateTimeField()
    actual_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='taken')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-scheduled_time']
    
    def __str__(self):
        return f"{self.medicine.name} - {self.status} on {self.scheduled_time.date()}"

class Prescription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prescriptions')
    doctor_name = models.CharField(max_length=100)
    clinic_hospital = models.CharField(max_length=100, blank=True)
    prescription_date = models.DateField()
    image = models.ImageField(upload_to='prescriptions/')
    notes = models.TextField(blank=True)
    is_processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-prescription_date']
    
    def __str__(self):
        return f"Prescription from {self.doctor_name} - {self.prescription_date}"
