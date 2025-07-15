
from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Weight tracking
    path('weight/add/', views.add_weight, name='add_weight'),
    path('weight/', views.weight_list, name='weight_list'),
    
    # Exercise tracking
    path('exercise/add/', views.add_exercise, name='add_exercise'),
    path('exercise/', views.exercise_list, name='exercise_list'),
    
    # Meal tracking
    path('meals/add/', views.add_meal, name='add_meal'),
    path('meals/', views.meals, name='meals'),
    
    # Vital signs
    path('vitals/add/', views.add_vitals, name='add_vitals'),
    path('vitals/', views.vitals_list, name='vitals_list'),
    
    # Goals
    path('goals/', views.goals, name='goals'),
    path('goals/add/', views.add_goal, name='add_goal'),
]
