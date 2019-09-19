from django.shortcuts import render, redirect
from .forms import WeightForm
from .models import Weight
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages


def index(request):
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

    form = WeightForm()
    return render(request, 'weight/weight.html', {'form': form})
