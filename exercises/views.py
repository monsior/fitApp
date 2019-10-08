from django.shortcuts import render, redirect
from .forms import ExerciseForm
from .models import Exercise
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages


def display_exercises(request):  # return a dictionary containing every user's exercise
    form = ExerciseForm()
    exercises = Exercise.objects.filter(username=request.user)
    exercises_list = []
    for exercise in exercises:
        exercises_list.append(exercise)
    args = {'form': form, 'exercises_list': exercises_list}
    return args


def add_exercise(request):
    instance = Exercise(username=request.user, date=timezone.now())
    form = ExerciseForm(data=request.POST, instance=instance)

    if request.method == 'POST':
        if form.is_valid():
            form.username = User
            form.date = timezone.now()
            form.save()
            messages.success(request, 'Exercise added!')
            return redirect('/exercises/')
        else:
            messages.warning(request, 'Exercise NOT added!')

    return render(request, 'exercises/exercises.html', display_exercises(request))
