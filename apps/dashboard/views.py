
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Avg, Count
from django.utils import timezone
from datetime import datetime, timedelta
from apps.tracker.models import WeightEntry, Exercise, Meal, HealthGoal, VitalSigns
from apps.accounts.models import UserProfile

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard:dashboard')
    return render(request, 'dashboard/home.html')

@login_required
def dashboard(request):
    # Get user profile
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    # Recent entries
    recent_weight = WeightEntry.objects.filter(user=request.user).first()
    recent_exercises = Exercise.objects.filter(user=request.user)[:3]
    recent_meals = Meal.objects.filter(user=request.user)[:3]
    
    # Today's stats
    today = timezone.now().date()
    today_calories = Meal.objects.filter(
        user=request.user,
        date_consumed__date=today
    ).aggregate(Sum('calories'))['calories__sum'] or 0
    
    today_exercise_minutes = Exercise.objects.filter(
        user=request.user,
        date_performed__date=today
    ).aggregate(Sum('duration_minutes'))['duration_minutes__sum'] or 0
    
    # This week's stats
    week_start = today - timedelta(days=today.weekday())
    week_exercises = Exercise.objects.filter(
        user=request.user,
        date_performed__date__gte=week_start
    ).count()
    
    # Active goals
    active_goals = HealthGoal.objects.filter(
        user=request.user,
        status='active'
    ).order_by('target_date')[:3]
    
    # Weight trend (last 7 entries)
    weight_entries = WeightEntry.objects.filter(user=request.user)[:7]
    
    # Recent vital signs
    recent_vitals = VitalSigns.objects.filter(user=request.user).first()
    
    context = {
        'user_profile': user_profile,
        'recent_weight': recent_weight,
        'recent_exercises': recent_exercises,
        'recent_meals': recent_meals,
        'today_calories': today_calories,
        'today_exercise_minutes': today_exercise_minutes,
        'week_exercises': week_exercises,
        'active_goals': active_goals,
        'weight_entries': weight_entries,
        'recent_vitals': recent_vitals,
    }
    
    return render(request, 'dashboard/dashboard.html', context)

@login_required
def analytics(request):
    # Weight analytics
    weight_entries = WeightEntry.objects.filter(user=request.user).order_by('date_recorded')
    
    # Exercise analytics
    exercise_stats = Exercise.objects.filter(user=request.user).values('exercise_type').annotate(
        total_duration=Sum('duration_minutes'),
        total_calories=Sum('calories_burned'),
        count=Count('id')
    )
    
    # Meal analytics
    meal_stats = Meal.objects.filter(user=request.user).values('meal_type').annotate(
        avg_calories=Avg('calories'),
        total_calories=Sum('calories'),
        count=Count('id')
    )
    
    # Monthly trends
    last_30_days = timezone.now().date() - timedelta(days=30)
    monthly_calories = Meal.objects.filter(
        user=request.user,
        date_consumed__date__gte=last_30_days
    ).extra(
        select={'day': 'date(date_consumed)'}
    ).values('day').annotate(
        total_calories=Sum('calories')
    ).order_by('day')
    
    context = {
        'weight_entries': weight_entries,
        'exercise_stats': exercise_stats,
        'meal_stats': meal_stats,
        'monthly_calories': monthly_calories,
    }
    
    return render(request, 'dashboard/analytics.html', context)
