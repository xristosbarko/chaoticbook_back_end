from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from .models import Like
from .serializers import LikeSerializer


class LikeCreate(generics.CreateAPIView):
    """
    Add a Like.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = LikeSerializer


class LikeDelete(generics.DestroyAPIView):
    """
    Delete a Like.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = LikeSerializer

    def get_object(self):
        user = self.request.user
        post_id = self.kwargs["post_id"]
        like = get_object_or_404(Like, post=post_id, user=user)
        return like

    def perform_destroy(self, instance):
        user = self.request.user

        if user == instance.user:
            instance.delete()
        else:
            raise PermissionDenied(
                detail="You are not allowed to delete this like."
            )
