from rest_framework import serializers
from .models import SavedJob


class SavedJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedJob
        fields = ('id', 'user', 'job')
        read_only_fields = ('id', 'user')