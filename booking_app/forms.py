from .models import Appointment
from django import forms
from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS


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
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Please select another time and date\
                    combination and try again.",
            }
        }
