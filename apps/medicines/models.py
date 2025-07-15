from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

def get_medicine_upload_path(instance, filename):
    return f'medicine_images/{instance.user.username}/{filename}'

def get_prescription_upload_path(instance, filename):
    return f'prescriptions/{instance.user.username}/{filename}'

class Medicine(models.Model):
    FREQUENCY_CHOICES = [
        ('once_daily', 'Once Daily'),
        ('twice_daily', 'Twice Daily'),
        ('three_times', 'Three Times Daily'),
        ('four_times', 'Four Times Daily'),
        ('as_needed', 'As Needed'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]

    DOSAGE_UNITS = [
        ('mg', 'Milligrams'),
        ('g', 'Grams'),
        ('ml', 'Milliliters'),
        ('tablets', 'Tablets'),
        ('capsules', 'Capsules'),
        ('drops', 'Drops'),
        ('units', 'Units'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='medicines')
    name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=50)
    dosage_unit = models.CharField(max_length=20, choices=DOSAGE_UNITS, default='mg')
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    doctor_name = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    side_effects = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to=get_medicine_upload_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.dosage}{self.dosage_unit}"

class Prescription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prescriptions')
    title = models.CharField(max_length=200)
    doctor_name = models.CharField(max_length=100)
    clinic_hospital = models.CharField(max_length=100, blank=True)
    prescription_date = models.DateField()
    file = models.FileField(upload_to=get_prescription_upload_path)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-prescription_date']

    def __str__(self):
        return f"{self.user.username} - {self.title}"

class MedicationReminder(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='reminders')
    time = models.TimeField()
    is_active = models.BooleanField(default=True)
    notes = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['time']

    def __str__(self):
        return f"{self.medicine.name} at {self.time}"