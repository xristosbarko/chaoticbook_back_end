from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .filters import UserProfileFilter
from .models import Profile
from .serializers import (
    ProfileEditSerializer,
    ProfileSerializer,
    UserProfileSerializer,
)


class ProfileDetails(generics.RetrieveAPIView):
    """
    Get user profile.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = ProfileEditSerializer
    filter_backends = [UserProfileFilter]

    def get_object(self):
        user = self.request.query_params.get("user", None)
        if user:
            user = get_object_or_404(User, pk=user)
        else:
            user = self.request.user
        return get_object_or_404(Profile, user=user)


class ProfileCreate(generics.CreateAPIView):
    """
    Add user profile.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer


class ProfileEdit(generics.UpdateAPIView):
    """
    Edit user profile.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = ProfileEditSerializer

    def get_object(self):
        user = self.request.user
        profile = get_object_or_404(Profile, user=user)
        return profile


class getUserProfile(generics.RetrieveAPIView):
    """
    Get user profile.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer
    filter_backends = [UserProfileFilter]

    def get_object(self):
        user = self.request.query_params.get("user", None)
        if user:
            user = get_object_or_404(User, pk=user)
        else:
            user = self.request.user
        return user
