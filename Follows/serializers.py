from rest_framework import serializers
from .models import Follow
from rest_framework.exceptions import PermissionDenied, ValidationError
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class FollowingsSerializer(serializers.ModelSerializer):
	user_id = serializers.IntegerField(source='following.id')
	username = serializers.CharField(source='following.username')
	profile_picture = serializers.SerializerMethodField()
	follow = serializers.SerializerMethodField()

	class Meta:
		model = Follow
		fields = (
			'user_id',
			'username',
			'profile_picture',
			'follow',
		)

	def get_profile_picture(self, follow):
		picture_url = follow.following.profile_user.profile_picture.url
		return self.context.get('request').build_absolute_uri(picture_url)

	def get_follow(self, follow):
		request = self.context.get('request')
		check_follow = Follow.objects.filter(following=follow.following, follower=request.user)
		if check_follow.count():
			return {'sent': True, 'pending': check_follow[0].pending}
		else:
			return {'sent': False}

	def to_representation(self, follow):
		representation = super(FollowingsSerializer, self).to_representation(follow)
		request = self.context.get('request')
		if follow.following == request.user:
			representation.pop('follow')
		return representation


class FollowersSerializer(serializers.ModelSerializer):
	user_id = serializers.IntegerField(source='follower.id')
	username = serializers.CharField(source='follower.username')
	profile_picture = serializers.SerializerMethodField()
	follow = serializers.SerializerMethodField()

	class Meta:
		model = Follow
		fields = (
			'user_id',
			'username',
			'profile_picture',
			'follow',
		)

	def get_profile_picture(self, follow):
		picture_url = follow.follower.profile_user.profile_picture.url
		return self.context.get('request').build_absolute_uri(picture_url)

	def get_follow(self, follow):
		request = self.context.get('request')
		check_follow = Follow.objects.filter(following=follow.follower, follower=request.user)
		if check_follow.count():
			return {'sent': True, 'pending': check_follow[0].pending}
		else:
			return {'sent': False}

	def to_representation(self, follow):
		representation = super(FollowersSerializer, self).to_representation(follow)
		request = self.context.get('request')
		if follow.follower == request.user:
			representation.pop('follow')
		return representation


class FollowSerializer(serializers.ModelSerializer):
	user_id = serializers.PrimaryKeyRelatedField(source='following', queryset=User.objects.all())
	class Meta:
		model = Follow
		fields = (
			'id',
			'user_id',
		)

	def create(self, validated_data):
		request = self.context.get('request')

		validated_data["follower"] = request.user
		follow = Follow.objects.create(**validated_data)

		return follow

class FollowAcceptOrDeclineSerializer(serializers.ModelSerializer):
	accepted = serializers.SerializerMethodField()
	class Meta:
		model = Follow
		fields = (
			'accepted',
		)

	def get_accepted(self, follow):
		if follow.id:
			return True
		else:
			return False