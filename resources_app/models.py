from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

SUBJECTS = (
    ('0', 'English'),
    ('1', 'Maths'),
    ('2', 'History'),
    ('3', 'Geography'),
    ('4', 'Art'),
    ('5', 'Science'),
    ('6', 'Music'),
)


class Resource(models.Model):
    resource_name = models.CharField(max_length=80)
    subject = models.CharField(
        max_length=80, choices=SUBJECTS, default='0')
    description = models.CharField(max_length=150)
    file = models.FileField(upload_to='media/', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
