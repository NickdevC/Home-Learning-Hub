from .import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('appointments/', views.ViewAppointments.as_view(), name='appointments'),
    path('delete/<int:appointment_id>', views.delete_appointment, name='delete'),
    path('edit/<int:appointment_id>', views.edit_appointment, name='edit'),
]
