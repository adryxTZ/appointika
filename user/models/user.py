from django.contrib.auth.models import AbstractUser
from django.db import models

STATUS_CHOICES = (
    ('Active', 'Active'),
    ('Deleted', 'Deleted'),
    ('Blocked', 'Blocked'),
    ('Private', 'Private')
)


class User(AbstractUser):
    ROLE_CHOICES = (
        ("patient", "Patient"),
        ("doctor", "Doctor"),
        ("admin", "Admin"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="patient")
    phone = models.CharField(max_length=15, blank=True, null=True)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, default='Other')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
