
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from datetime import datetime, timedelta
from .models import WeightEntry, VitalSigns, Exercise, Meal, HealthGoal
from .forms import WeightEntryForm, VitalSignsForm, ExerciseForm, MealForm, HealthGoalForm

@login_required
def dashboard(request):
    # Get recent entries
    recent_weight = WeightEntry.objects.filter(user=request.user).first()
    recent_exercises = Exercise.objects.filter(user=request.user)[:5]
    recent_meals = Meal.objects.filter(user=request.user)[:5]
    active_goals = HealthGoal.objects.filter(user=request.user, status='active')[:3]
    
    # Calculate today's calories
    today = timezone.now().date()
    today_calories = Meal.objects.filter(
        user=request.user,
        date_consumed__date=today
    ).aggregate(models.Sum('calories'))['calories__sum'] or 0
    
    context = {
        'recent_weight': recent_weight,
        'recent_exercises': recent_exercises,
        'recent_meals': recent_meals,
        'active_goals': active_goals,
        'today_calories': today_calories,
    }
    return render(request, 'tracker/dashboard.html', context)

@login_required
def add_weight(request):
    if request.method == 'POST':
        form = WeightEntryForm(request.POST)
        if form.is_valid():
            weight_entry = form.save(commit=False)
            weight_entry.user = request.user
            weight_entry.save()
            messages.success(request, 'Weight entry added successfully!')
            return redirect('tracker:weight_list')
    else:
        form = WeightEntryForm()
    
    return render(request, 'tracker/add_weight.html', {'form': form})

@login_required
def weight_list(request):
    weight_entries = WeightEntry.objects.filter(user=request.user)
    return render(request, 'tracker/weight_list.html', {'weight_entries': weight_entries})

@login_required
def add_exercise(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.user = request.user
            exercise.save()
            messages.success(request, 'Exercise logged successfully!')
            return redirect('tracker:exercise_list')
    else:
        form = ExerciseForm()
    
    return render(request, 'tracker/add_exercise.html', {'form': form})

@login_required
def exercise_list(request):
    exercises = Exercise.objects.filter(user=request.user)
    return render(request, 'tracker/exercise_list.html', {'exercises': exercises})

@login_required
def add_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user
            meal.save()
            messages.success(request, 'Meal logged successfully!')
            return redirect('tracker:meals')
    else:
        form = MealForm()
    
    return render(request, 'tracker/add_meal.html', {'form': form})

@login_required
def meals(request):
    meals = Meal.objects.filter(user=request.user)
    return render(request, 'tracker/meals.html', {'meals': meals})

@login_required
def goals(request):
    goals = HealthGoal.objects.filter(user=request.user)
    return render(request, 'tracker/goals.html', {'goals': goals})

@login_required
def add_goal(request):
    if request.method == 'POST':
        form = HealthGoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            messages.success(request, 'Goal created successfully!')
            return redirect('tracker:goals')
    else:
        form = HealthGoalForm()
    
    return render(request, 'tracker/add_goal.html', {'form': form})

@login_required
def add_vitals(request):
    if request.method == 'POST':
        form = VitalSignsForm(request.POST)
        if form.is_valid():
            vitals = form.save(commit=False)
            vitals.user = request.user
            vitals.save()
            messages.success(request, 'Vital signs recorded successfully!')
            return redirect('tracker:vitals_list')
    else:
        form = VitalSignsForm()
    
    return render(request, 'tracker/add_vitals.html', {'form': form})

@login_required
def vitals_list(request):
    vitals = VitalSigns.objects.filter(user=request.user)
    return render(request, 'tracker/vitals_list.html', {'vitals': vitals})
