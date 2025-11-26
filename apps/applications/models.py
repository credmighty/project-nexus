from django.db import models
from jobs.models import Job
from django.conf import settings

class Application(models.Model):
    STATUS = (
        ('applied', 'Applied'),
        ('reviewed', 'Reviewed'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    resume = models.FileField(upload_to="resumes/")
    cover_letter = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default="applied")
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant} --> {self.job}"
