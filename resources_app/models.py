from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Custom choices
SUBJECTS = (
    ('0', 'English'),
    ('1', 'Maths'),
    ('2', 'History'),
    ('3', 'Geography'),
    ('4', 'Art'),
    ('5', 'Science'),
    ('6', 'Music'),
)


# Resource class for admins to upload a resource to library
class Resource(models.Model):
    resource_name = models.CharField(max_length=80)
    subject = models.CharField(
        max_length=80, choices=SUBJECTS, default='0')
    description = models.CharField(max_length=150)
    file = CloudinaryField(resource_type='raw', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
