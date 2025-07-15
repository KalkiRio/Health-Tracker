
from django import forms
from .models import WeightEntry, VitalSigns, Exercise, Meal, HealthGoal

class WeightEntryForm(forms.ModelForm):
    class Meta:
        model = WeightEntry
        fields = ['weight', 'date_recorded', 'notes']
        widgets = {
            'date_recorded': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'weight': forms.NumberInput(attrs={'step': '0.1', 'placeholder': 'Weight in kg'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Optional notes...'}),
        }

class VitalSignsForm(forms.ModelForm):
    class Meta:
        model = VitalSigns
        fields = ['systolic_bp', 'diastolic_bp', 'heart_rate', 'blood_glucose', 'temperature', 'date_recorded', 'notes']
        widgets = {
            'date_recorded': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'systolic_bp': forms.NumberInput(attrs={'placeholder': 'e.g., 120'}),
            'diastolic_bp': forms.NumberInput(attrs={'placeholder': 'e.g., 80'}),
            'heart_rate': forms.NumberInput(attrs={'placeholder': 'e.g., 75'}),
            'blood_glucose': forms.NumberInput(attrs={'step': '0.1', 'placeholder': 'e.g., 90.5'}),
            'temperature': forms.NumberInput(attrs={'step': '0.1', 'placeholder': 'e.g., 36.5'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['exercise_type', 'exercise_name', 'duration_minutes', 'calories_burned', 'date_performed', 'notes']
        widgets = {
            'date_performed': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'exercise_name': forms.TextInput(attrs={'placeholder': 'e.g., Morning Jog'}),
            'duration_minutes': forms.NumberInput(attrs={'placeholder': 'Duration in minutes'}),
            'calories_burned': forms.NumberInput(attrs={'placeholder': 'Estimated calories burned'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Exercise details, intensity, etc.'}),
        }

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['meal_name', 'meal_type', 'calories', 'protein', 'carbs', 'fat', 'date_consumed', 'notes']
        widgets = {
            'date_consumed': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'meal_name': forms.TextInput(attrs={'placeholder': 'e.g., Grilled Chicken Salad'}),
            'calories': forms.NumberInput(attrs={'placeholder': 'Estimated calories'}),
            'protein': forms.NumberInput(attrs={'step': '0.1', 'placeholder': 'Protein in grams'}),
            'carbs': forms.NumberInput(attrs={'step': '0.1', 'placeholder': 'Carbs in grams'}),
            'fat': forms.NumberInput(attrs={'step': '0.1', 'placeholder': 'Fat in grams'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Meal details, ingredients, etc.'}),
        }

class HealthGoalForm(forms.ModelForm):
    class Meta:
        model = HealthGoal
        fields = ['goal_type', 'title', 'description', 'target_value', 'current_value', 'unit', 'target_date', 'status']
        widgets = {
            'target_date': forms.DateInput(attrs={'type': 'date'}),
            'title': forms.TextInput(attrs={'placeholder': 'e.g., Lose 10kg'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe your goal...'}),
            'target_value': forms.NumberInput(attrs={'step': '0.1'}),
            'current_value': forms.NumberInput(attrs={'step': '0.1'}),
            'unit': forms.TextInput(attrs={'placeholder': 'e.g., kg, minutes, reps'}),
        }
