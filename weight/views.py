from django.shortcuts import render, redirect
from .forms import WeightForm
from .models import Weight
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages


def display_weights(request):  # return a dictionary containing every user's weight
    form = WeightForm()
    weights = Weight.objects.filter(username=request.user)
    weights = reversed(weights)  # we want to display weights chronologically
    args = {'form': form, 'weights': weights}
    return args


def add_weight(request):
    instance = Weight(username=request.user, date=timezone.now())

    if request.method == 'POST':
        form = WeightForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.username = User
            form.date = timezone.now()
            form.save()
            messages.success(request, 'Weight added!')
            return redirect('/weight/')
        else:
            messages.warning(request, 'Weight NOT added!')

    return render(request, 'weight/weight.html', display_weights(request))
