
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Medicine, MedicationReminder, MedicationLog, Prescription
from .forms import MedicineForm, MedicationReminderForm, PrescriptionForm

@login_required
def medicine_list(request):
    medicines = Medicine.objects.filter(user=request.user)
    
    # Filter by status
    status = request.GET.get('status')
    if status == 'active':
        medicines = medicines.filter(is_active=True)
    elif status == 'inactive':
        medicines = medicines.filter(is_active=False)
    
    return render(request, 'medicines/medicine_list.html', {'medicines': medicines, 'current_status': status})

@login_required
def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST, request.FILES)
        if form.is_valid():
            medicine = form.save(commit=False)
            medicine.user = request.user
            medicine.save()
            messages.success(request, 'Medicine added successfully!')
            return redirect('medicines:list')
    else:
        form = MedicineForm()
    
    return render(request, 'medicines/add_medicine.html', {'form': form})

@login_required
def medicine_detail(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id, user=request.user)
    reminders = medicine.reminders.filter(is_active=True)
    recent_logs = medicine.logs.all()[:10]
    
    context = {
        'medicine': medicine,
        'reminders': reminders,
        'recent_logs': recent_logs,
    }
    
    return render(request, 'medicines/medicine_detail.html', context)

@login_required
def add_reminder(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id, user=request.user)
    
    if request.method == 'POST':
        form = MedicationReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.medicine = medicine
            reminder.save()
            messages.success(request, 'Reminder added successfully!')
            return redirect('medicines:detail', medicine_id=medicine.id)
    else:
        form = MedicationReminderForm()
    
    return render(request, 'medicines/add_reminder.html', {'form': form, 'medicine': medicine})

@login_required
def medication_schedule(request):
    today = timezone.now().date()
    
    # Get all active medicines with their reminders
    medicines = Medicine.objects.filter(user=request.user, is_active=True).prefetch_related('reminders')
    
    # Create schedule for today
    schedule = []
    for medicine in medicines:
        for reminder in medicine.reminders.filter(is_active=True):
            schedule.append({
                'medicine': medicine,
                'time': reminder.time,
                'reminder_id': reminder.id,
            })
    
    # Sort by time
    schedule.sort(key=lambda x: x['time'])
    
    # Get today's logs
    today_logs = MedicationLog.objects.filter(
        medicine__user=request.user,
        scheduled_time__date=today
    )
    
    context = {
        'schedule': schedule,
        'today_logs': today_logs,
        'today': today,
    }
    
    return render(request, 'medicines/medication_schedule.html', context)

@login_required
def log_medication(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id, user=request.user)
    
    if request.method == 'POST':
        status = request.POST.get('status', 'taken')
        notes = request.POST.get('notes', '')
        
        # Create medication log
        MedicationLog.objects.create(
            medicine=medicine,
            scheduled_time=timezone.now(),
            actual_time=timezone.now() if status == 'taken' else None,
            status=status,
            notes=notes
        )
        
        messages.success(request, f'Medication {status} logged successfully!')
        return redirect('medicines:schedule')
    
    return render(request, 'medicines/log_medication.html', {'medicine': medicine})

@login_required
def prescriptions(request):
    prescriptions_list = Prescription.objects.filter(user=request.user)
    
    paginator = Paginator(prescriptions_list, 10)
    page_number = request.GET.get('page')
    prescriptions = paginator.get_page(page_number)
    
    return render(request, 'medicines/prescriptions.html', {'prescriptions': prescriptions})

@login_required
def upload_prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, request.FILES)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.user = request.user
            prescription.save()
            messages.success(request, 'Prescription uploaded successfully!')
            return redirect('medicines:prescriptions')
    else:
        form = PrescriptionForm()
    
    return render(request, 'medicines/upload_prescription.html', {'form': form})
