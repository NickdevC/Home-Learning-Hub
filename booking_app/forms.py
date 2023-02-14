from .models import Appointment
from django import forms


# Date selector
class DateInput(forms.DateInput):
    input_type = 'date'


# Appointment form
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'date': DateInput(),
        }
