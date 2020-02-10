from rest_framework.filters import BaseFilterBackend
import coreapi
from ChaoticBook.permissions import isFollowing
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class PostListFilter(BaseFilterBackend):
	def get_schema_fields(self, view):
		params = ['user']
		QueryParameters = []
		for param in params:
			QueryParameters.append(coreapi.Field(name=param, required=False, location='query'))
		return QueryParameters

	def filter_queryset(self, request, queryset, view):
		user = request.user
		following = request.query_params.get('user', None)
		if following:
			following = get_object_or_404(User, pk=following)
			isFollowing(following, user)
			return Post.objects.filter(user=following).order_by('-timestamp')
		else:
			return Post.objects.filter(user=user).order_by('-timestamp')