from django.shortcuts import render, redirect
from .forms import WeightForm
from .models import Weight
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages


def add_missing_dates(dates_array, weights_array):
    for i in range(1, len(dates_array)):
        if (dates_array[i]-dates_array[i-1]).days > 1:
            for j in range(0, (dates_array[i]-dates_array[i-1]).days-1):
                dates_array.insert(i+j, dates_array[i-1] + timezone.timedelta(days=1+j))
                weights_array.insert(i + j, weights_array[i - 1])


def format_dates(dates_array):
    for i in range(0, len(dates_array)):
        dates_array[i] = (str(dates_array[i].day) + "-" + str(dates_array[i].month) + "-" + str(dates_array[i].year))


def display_weights(request):  # return a dictionary containing every user's weight
    form = WeightForm()
    weights = Weight.objects.filter(username=request.user).order_by('date')
    weight_values = []
    date_labels = []
    for weight in weights:
        weight_values.append(int(weight.weight))
        date_labels.append(weight.date)
    if len(date_labels) >= 2:
        add_missing_dates(date_labels, weight_values)
    format_dates(date_labels)
    args = {'form': form, 'weight_values': weight_values, 'date_labels': date_labels}
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
