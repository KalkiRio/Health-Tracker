
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from django.utils import timezone
from .models import MedicalReport, Appointment
from .forms import MedicalReportForm, AppointmentForm

@login_required
def profile(request):
    # Get user's medical profile data from UserProfile
    user_profile = request.user.userprofile
    context = {
        'user_profile': user_profile,
        'recent_reports': request.user.medical_reports.all()[:5],
        'upcoming_appointments': request.user.appointments.filter(
            appointment_date__gte=timezone.now(),
            status='scheduled'
        )[:5]
    }
    return render(request, 'medical/medical_profile.html', context)

@login_required
def reports(request):
    reports_list = MedicalReport.objects.filter(user=request.user)
    
    # Filter by report type if specified
    report_type = request.GET.get('type')
    if report_type:
        reports_list = reports_list.filter(report_type=report_type)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        reports_list = reports_list.filter(
            title__icontains=search_query
        )
    
    paginator = Paginator(reports_list, 10)
    page_number = request.GET.get('page')
    reports = paginator.get_page(page_number)
    
    context = {
        'reports': reports,
        'report_types': MedicalReport.REPORT_TYPES,
        'current_type': report_type,
        'search_query': search_query,
    }
    
    return render(request, 'medical/reports_list.html', context)

@login_required
def upload_report(request):
    if request.method == 'POST':
        form = MedicalReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            messages.success(request, 'Medical report uploaded successfully!')
            return redirect('medical:reports')
    else:
        form = MedicalReportForm()
    
    return render(request, 'medical/upload_report.html', {'form': form})

@login_required
def report_detail(request, report_id):
    report = get_object_or_404(MedicalReport, id=report_id, user=request.user)
    return render(request, 'medical/report_detail.html', {'report': report})

@login_required
def download_report(request, report_id):
    report = get_object_or_404(MedicalReport, id=report_id, user=request.user)
    
    try:
        response = HttpResponse(report.file.read(), content_type='application/force-download')
        response['Content-Disposition'] = f'attachment; filename="{report.file.name}"'
        return response
    except Exception:
        raise Http404("File not found")

@login_required
def appointments(request):
    appointments_list = Appointment.objects.filter(user=request.user)
    
    # Filter by status if specified
    status = request.GET.get('status')
    if status:
        appointments_list = appointments_list.filter(status=status)
    
    paginator = Paginator(appointments_list, 10)
    page_number = request.GET.get('page')
    appointments = paginator.get_page(page_number)
    
    context = {
        'appointments': appointments,
        'status_choices': Appointment.STATUS_CHOICES,
        'current_status': status,
    }
    
    return render(request, 'medical/appointments_list.html', context)

@login_required
def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            messages.success(request, 'Appointment scheduled successfully!')
            return redirect('medical:appointments')
    else:
        form = AppointmentForm()
    
    return render(request, 'medical/add_appointment.html', {'form': form})

@login_required
def appointment_detail(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, user=request.user)
    return render(request, 'medical/appointment_detail.html', {'appointment': appointment})
