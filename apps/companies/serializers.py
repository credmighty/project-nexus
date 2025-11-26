form rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'logo', 'description', 'created_by')
        read_only_fields = ('id', 'created_by')