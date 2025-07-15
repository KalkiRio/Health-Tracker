from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Avg, Count
from django.utils import timezone
from datetime import datetime, timedelta
from apps.tracker.models import WeightEntry, Exercise, Meal, HealthGoal, VitalSigns
from apps.accounts.models import UserProfile

@login_required
def home(request):
    user = request.user
    today = date.today()
    week_ago = today - timedelta(days=7)

    # Get user profile
    user_profile = user.userprofile

    # Recent weight entries
    recent_weights = user.weight_entries.all()[:5] if hasattr(user, 'weight_entries') else []

    # Recent exercises
    recent_exercises = user.exercises.all()[:5] if hasattr(user, 'exercises') else []

    # This week's statistics
    week_stats = {}
    if hasattr(user, 'exercises'):
        week_stats['total_exercises'] = user.exercises.filter(date_performed__gte=week_ago).count()
        week_stats['total_calories'] = user.exercises.filter(
            date_performed__gte=week_ago,
            calories_burned__isnull=False
        ).aggregate(Sum('calories_burned'))['calories_burned__sum'] or 0
    else:
        week_stats['total_exercises'] = 0
        week_stats['total_calories'] = 0

    if hasattr(user, 'water_intakes'):
        week_stats['avg_water'] = user.water_intakes.filter(date_recorded__gte=week_ago).aggregate(
            Avg('amount_ml'))['amount_ml__avg'] or 0
    else:
        week_stats['avg_water'] = 0

    if hasattr(user, 'sleep_records'):
        week_stats['avg_sleep'] = user.sleep_records.filter(sleep_date__gte=week_ago).aggregate(
            Avg('hours_slept'))['hours_slept__avg'] or 0
    else:
        week_stats['avg_sleep'] = 0

    # Upcoming appointments
    upcoming_appointments = []
    if hasattr(user, 'appointments'):
        upcoming_appointments = user.appointments.filter(
            appointment_date__gte=timezone.now(),
            status='scheduled'
        )[:3]

    # Active medicines
    active_medicines = []
    if hasattr(user, 'medicines'):
        active_medicines = user.medicines.filter(is_active=True)[:5]

    context = {
        'user_profile': user_profile,
        'recent_weights': recent_weights,
        'recent_exercises': recent_exercises,
        'week_stats': week_stats,
        'upcoming_appointments': upcoming_appointments,
        'active_medicines': active_medicines,
        'today': today,
    }

    return render(request, 'dashboard/dashboard.html', context)

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
```

```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Avg, Count
from django.utils import timezone
from datetime import datetime, timedelta, date
from apps.tracker.models import WeightEntry, Exercise, Meal, HealthGoal, VitalSigns
from apps.accounts.models import UserProfile

@login_required
def home(request):
    user = request.user
    today = date.today()
    week_ago = today - timedelta(days=7)

    # Get user profile
    try:
        user_profile = user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=user)


    # Recent weight entries
    recent_weights = user.weightentry_set.all()[:5]

    # Recent exercises
    recent_exercises = user.exercise_set.all()[:5]

    # This week's statistics
    week_stats = {}

    week_stats['total_exercises'] = user.exercise_set.filter(date_performed__gte=week_ago).count()
    week_stats['total_calories'] = user.exercise_set.filter(
        date_performed__gte=week_ago,
        calories_burned__isnull=False
    ).aggregate(Sum('calories_burned'))['calories_burned__sum'] or 0



    week_stats['avg_water'] = 0

    week_stats['avg_sleep'] = 0

    # Upcoming appointments
    upcoming_appointments = []


    # Active medicines
    active_medicines = []


    context = {
        'user_profile': user_profile,
        'recent_weights': recent_weights,
        'recent_exercises': recent_exercises,
        'week_stats': week_stats,
        'upcoming_appointments': upcoming_appointments,
        'active_medicines': active_medicines,
        'today': today,
    }

    return render(request, 'dashboard/dashboard.html', context)

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