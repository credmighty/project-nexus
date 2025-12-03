from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('job_seeker', 'Job Seeker'),
        ('recruiter', 'Recruiter'),
        ('admin', 'Admin'),
    )

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    role = models.CharField(max_length=20, choice=ROLE_CHOICES)
    email_verified = models.BooleanField(default=False, db_index=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
