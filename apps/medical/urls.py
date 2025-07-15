
from django.urls import path
from . import views

app_name = 'medical'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('reports/', views.reports, name='reports'),
    path('reports/upload/', views.upload_report, name='upload_report'),
    path('reports/<int:report_id>/', views.report_detail, name='report_detail'),
    path('reports/<int:report_id>/download/', views.download_report, name='download_report'),
    path('appointments/', views.appointments, name='appointments'),
    path('appointments/add/', views.add_appointment, name='add_appointment'),
    path('appointments/<int:appointment_id>/', views.appointment_detail, name='appointment_detail'),
]
