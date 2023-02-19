from django.contrib import admin
from .models import Resource


# Admin contact from / taking contact model
@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    search_fields = ('resource_name', 'subject',)
    list_display = ('subject', 'resource_name', 'created_on')
