from .import views
from django.urls import path


urlpatterns = [
    path('resources/', views.DisplayResource.as_view(), name='resources'),
    path('edit_resources/', views.uploadResource, name='edit_resources')
]
