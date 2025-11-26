from django.db import models
from companies import Company

class Job(models.Model):
    JOB_TYPES = (
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
    )

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=JOB_TYPES)
    salary_range = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
