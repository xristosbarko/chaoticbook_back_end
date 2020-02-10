from rest_framework.filters import BaseFilterBackend
import coreapi
from .models import Follow
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class FollowingsListFilter(BaseFilterBackend):
	def get_schema_fields(self, view):
		params = ['user_id']
		QueryParameters = []
		for param in params:
			QueryParameters.append(coreapi.Field(name=param, required=False, location='query'))
		return QueryParameters

	def filter_queryset(self, request, queryset, view):
		user_id = request.query_params.get('user_id', None)
		if user_id:
			user = get_object_or_404(User, pk=user_id)
		else:
			user = request.user
		return Follow.objects.filter(pending=False, follower=user)

class FollowersListFilter(BaseFilterBackend):
	def get_schema_fields(self, view):
		params = ['pending', 'user_id']
		QueryParameters = []
		for param in params:
			QueryParameters.append(coreapi.Field(name=param, required=False, location='query'))
		return QueryParameters

	def filter_queryset(self, request, queryset, view):
		pending = request.query_params.get('pending', False)

		if pending == 'True':
			user = request.user
			return Follow.objects.filter(pending=True, following=user)
		else:
			user_id = request.query_params.get('user_id', None)
			if user_id:
				user = get_object_or_404(User, pk=user_id)
			else:
				user = request.user
			return Follow.objects.filter(pending=False, following=user)

class FollowAcceptOrDeclineFilter(BaseFilterBackend):
	def get_schema_fields(self, view):
		params = ['decline']
		QueryParameters = []
		for param in params:
			QueryParameters.append(coreapi.Field(name=param, required=False, location='query'))
		return QueryParameters