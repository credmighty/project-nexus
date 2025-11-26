from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserDetailSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework import permissions

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user