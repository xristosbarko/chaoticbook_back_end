from .models import Follow
from .serializers import (
	FollowSerializer, FollowingsSerializer,
	FollowersSerializer, FollowAcceptOrDeclineSerializer
)
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied, ValidationError
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .filters import FollowingsListFilter, FollowersListFilter, FollowAcceptOrDeclineFilter

class FollowingsList(generics.ListAPIView):
	"""
	Returns a list of all the Followings.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Follow.objects.all()
	serializer_class = FollowingsSerializer
	filter_backends = [FollowingsListFilter]


class FollowersList(generics.ListAPIView):
	"""
	Returns a list of all the Followers.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Follow.objects.all()
	serializer_class = FollowersSerializer
	filter_backends = [FollowersListFilter]


class FollowCreate(generics.CreateAPIView):
	"""
	Add a Follow.
	"""
	permission_classes = [IsAuthenticated]
	serializer_class = FollowSerializer

	def perform_create(self, serializer):
		user = self.request.user
		following = serializer.validated_data['following']
		if user == following:
			raise ValidationError(detail='You can\'t follow yourself.')
		serializer.save()


class FollowDelete(generics.DestroyAPIView):
	"""
	Delete a Follow.
	"""
	permission_classes = [IsAuthenticated]
	serializer_class = FollowSerializer

	def get_object(self):
		user = self.request.user
		user_id = self.kwargs['user_id']
		follow = get_object_or_404(Follow, following=user_id, follower=user)
		return follow

class FollowAcceptOrDecline(generics.RetrieveAPIView):
	"""
	Accept a Follow.
	"""
	permission_classes = [IsAuthenticated]
	serializer_class = FollowAcceptOrDeclineSerializer
	filter_backends = [FollowAcceptOrDeclineFilter]

	def get_object(self):
		user = self.request.user
		user_id = self.kwargs['user_id']
		decline = self.request.query_params.get('decline', False)
		follow = get_object_or_404(Follow, following=user, follower=user_id, pending=True)
		if decline != 'True':
			follow.pending = False
			follow.save()
		else:
			follow.delete()
		return follow