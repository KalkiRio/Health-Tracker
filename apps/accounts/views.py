
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db import transaction
from .models import UserProfile, MedicalProfile, UserHealthProfile
from .forms import UserRegistrationForm, UserProfileForm, MedicalProfileForm, UserHealthProfileForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                user = form.save()
                # Create associated profiles
                UserProfile.objects.create(user=user)
                MedicalProfile.objects.create(user=user)
                UserHealthProfile.objects.create(user=user)
                
                login(request, user)
                messages.success(request, 'Registration successful! Please complete your profile.')
                return redirect('accounts:profile')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    medical_profile, created = MedicalProfile.objects.get_or_create(user=request.user)
    health_profile, created = UserHealthProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        medical_form = MedicalProfileForm(request.POST, instance=medical_profile)
        health_form = UserHealthProfileForm(request.POST, instance=health_profile)
        
        if user_form.is_valid() and medical_form.is_valid() and health_form.is_valid():
            user_form.save()
            medical_form.save()
            health_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('accounts:profile')
    else:
        user_form = UserProfileForm(instance=user_profile)
        medical_form = MedicalProfileForm(instance=medical_profile)
        health_form = UserHealthProfileForm(instance=health_profile)
    
    context = {
        'user_form': user_form,
        'medical_form': medical_form,
        'health_form': health_form,
    }
    return render(request, 'registration/profile.html', context)

@login_required
def medical_profile(request):
    medical_profile, created = MedicalProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = MedicalProfileForm(request.POST, instance=medical_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medical profile updated successfully!')
            return redirect('medical:profile')
    else:
        form = MedicalProfileForm(instance=medical_profile)
    
    return render(request, 'medical/medical_profile.html', {'form': form})
