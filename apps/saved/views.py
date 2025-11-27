from django.shortcuts import render
from rest_framework import viewsets
from rest_framework. permissions import IsAuthenticated
from .models import SavedJob
from .serializers import SavedJobSerializer


class SavedJobViewSet(viewsets.ModelViewSet):
    serializer_class = SavedJobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SavedJob.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Create your views here.
