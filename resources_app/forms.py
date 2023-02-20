from .models import Resource
from django import forms
from django.forms import ModelForm


# Resource form
class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = '__all__'
