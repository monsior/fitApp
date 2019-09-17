from django.shortcuts import render
from .models import Weight


def index(request):
    return render(request, 'weight/weight.html')
