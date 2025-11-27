from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'job', 'applicant', 'resume', 'cover_letter', 'status', 'applied_at')
        read_only_fields = ('id', 'applicant', 'status', 'applied_at')