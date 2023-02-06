from django.contrib import admin
from .models import Appointment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Appointment)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('teacher_name', 'date', 'time', 'child_name')
    search_fields = ('child_name', 'teacher_name', 'date')
    summernote_fields = ('comment')
