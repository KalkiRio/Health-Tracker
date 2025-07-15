
from django.contrib import admin
from .models import Medicine, Prescription, MedicationReminder

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'dosage', 'dosage_unit', 'frequency', 'start_date', 'is_active']
    list_filter = ['frequency', 'dosage_unit', 'is_active', 'start_date']
    search_fields = ['user__username', 'name', 'doctor_name']
    date_hierarchy = 'start_date'
    ordering = ['-created_at']

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'doctor_name', 'clinic_hospital', 'prescription_date']
    list_filter = ['prescription_date']
    search_fields = ['user__username', 'title', 'doctor_name', 'clinic_hospital']
    date_hierarchy = 'prescription_date'
    ordering = ['-prescription_date']

@admin.register(MedicationReminder)
class MedicationReminderAdmin(admin.ModelAdmin):
    list_display = ['medicine', 'time', 'is_active']
    list_filter = ['is_active', 'time']
    search_fields = ['medicine__name', 'medicine__user__username']
    ordering = ['time']
