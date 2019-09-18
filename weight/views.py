from django.shortcuts import render
from .forms import WeightForm
from .models import Weight
from django.contrib.auth.models import User
from django.utils import timezone


def index(request):
    instance = Weight(username=request.user, date=timezone.now())

    if request.method == 'POST':
        form = WeightForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.username = User
            form.date = timezone.now()
            form.save()

    form = WeightForm()
    return render(request, 'weight/weight.html', {'form': form})
