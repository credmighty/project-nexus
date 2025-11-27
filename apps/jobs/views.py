from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Job
from .serializers import JobSerializer
from common.permissions import IsRecruiter, IsOwnerOrReadOnly

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.filters(is_active=True).order_by('-created_at')
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filter.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'location', 'company__name']
    ordering_fields = ['created_at', 'title']

    def perform_create(self, serializer):
        # only recruiters create jobs; assume company field is validated to belong to recruiter
        serializer.save()
