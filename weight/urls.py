from django.urls import path

from . import views

urlpatterns = [
    path('', views.add_weight, name='add_weight'),
]