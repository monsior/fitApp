from django import forms
from .models import Weight


class DateInput(forms.DateInput):
    input_type = 'date'


class WeightForm(forms.ModelForm):

    class Meta:
        model = Weight
        widgets = {'date': DateInput()}
        fields = {'weight', 'date'}