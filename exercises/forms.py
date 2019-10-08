from django import forms
from .models import Exercise


class DateInput(forms.DateInput):
    input_type = 'date'


class ExerciseForm(forms.ModelForm):

    class Meta:
        model = Exercise
        widgets = {'date': DateInput()}
        fields = {'exercise', 'weight', 'series', 'reps', 'date'}
