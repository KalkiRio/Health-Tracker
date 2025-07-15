
from django.contrib import admin
from .models import MedicalReport, Appointment

@admin.register(MedicalReport)
class MedicalReportAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'report_type', 'doctor_name', 'report_date', 'upload_date']
    list_filter = ['report_type', 'report_date', 'upload_date']
    search_fields = ['user__username', 'title', 'doctor_name', 'clinic_hospital']
    date_hierarchy = 'report_date'
    ordering = ['-report_date']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'doctor_name', 'clinic_hospital', 'appointment_date', 'status']
    list_filter = ['status', 'appointment_date']
    search_fields = ['user__username', 'doctor_name', 'clinic_hospital', 'reason']
    date_hierarchy = 'appointment_date'
    ordering = ['-appointment_date']
