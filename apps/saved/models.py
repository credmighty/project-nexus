from django.db import models
from django.conf import settings
from jobs.models import Job


class SavedJob(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'job')
    
    def __str__(self):
        return f"{self.user} saved {self.job}"
