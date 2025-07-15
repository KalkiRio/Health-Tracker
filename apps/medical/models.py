
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import os

def get_report_upload_path(instance, filename):
    return f'medical_reports/{instance.user.username}/{instance.report_type}/{filename}'

class MedicalReport(models.Model):
    REPORT_TYPES = [
        ('lab', 'Lab Report'),
        ('xray', 'X-Ray'),
        ('prescription', 'Prescription'),
        ('scan', 'CT/MRI Scan'),
        ('other', 'Other Document'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='medical_reports')
    title = models.CharField(max_length=200)
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    file = models.FileField(upload_to=get_report_upload_path)
    description = models.TextField(blank=True)
    doctor_name = models.CharField(max_length=100, blank=True)
    clinic_hospital = models.CharField(max_length=100, blank=True)
    report_date = models.DateField()
    upload_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-report_date']
    
    def __str__(self):
        return f"{self.user.username} - {self.title}"
    
    def get_file_extension(self):
        return os.path.splitext(self.file.name)[1].lower()
    
    def is_image(self):
        return self.get_file_extension() in ['.jpg', '.jpeg', '.png', '.gif']
    
    def is_pdf(self):
        return self.get_file_extension() == '.pdf'

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('rescheduled', 'Rescheduled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    doctor_name = models.CharField(max_length=100)
    clinic_hospital = models.CharField(max_length=100)
    appointment_date = models.DateTimeField()
    duration_minutes = models.IntegerField(default=30)
    reason = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    reminder_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['appointment_date']
    
    def __str__(self):
        return f"{self.user.username} - {self.doctor_name} on {self.appointment_date.date()}"
    
    @property
    def is_upcoming(self):
        return self.appointment_date > timezone.now() and self.status == 'scheduled'
