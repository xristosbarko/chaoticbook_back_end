from rest_framework.filters import BaseFilterBackend
import coreapi
from .models import Profile
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class UserProfileFilter(BaseFilterBackend):
	def get_schema_fields(self, view):
		params = ['user']
		QueryParameters = []
		for param in params:
			QueryParameters.append(coreapi.Field(name=param, required=False, location='query'))
		return QueryParameters