
from django.urls import path
from . import views

app_name = 'medicines'

urlpatterns = [
    path('', views.medicine_list, name='list'),
    path('add/', views.add_medicine, name='add'),
    path('<int:medicine_id>/', views.medicine_detail, name='detail'),
    path('<int:medicine_id>/reminder/', views.add_reminder, name='add_reminder'),
    path('<int:medicine_id>/log/', views.log_medication, name='log_medication'),
    path('schedule/', views.medication_schedule, name='schedule'),
    path('prescriptions/', views.prescriptions, name='prescriptions'),
    path('prescriptions/upload/', views.upload_prescription, name='upload_prescription'),
]
