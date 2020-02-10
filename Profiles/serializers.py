from rest_framework import serializers
from .models import Profile
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from Posts.serializers import PostSerializer


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = (
			'birth_date',
			'gender',
			'profile_picture',
			'bio',
		)

	def create(self, validated_data):
		request = self.context.get('request')

		validated_data["user"] = request.user
		profile = Profile.objects.create(**validated_data)

		return profile


class ProfileEditSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = (
			'profile_picture',
			'bio',
		)

	def update(self, instance, validated_data):
		request = self.context.get('request')

		if request.user == instance.user:
			instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
			instance.bio = validated_data.get('bio', '')
			instance.save()
			return instance
		else:
			return HttpResponseForbidden()



class UserProfileSerializer(serializers.ModelSerializer):
	profile_picture = serializers.SerializerMethodField()
	bio = serializers.StringRelatedField(source='profile_user.bio')
	posts_count = serializers.SerializerMethodField()
	followers_count = serializers.SerializerMethodField()
	followings_count = serializers.SerializerMethodField()

	class Meta:
		model = User
		fields = (
			'id',
			'username',
			'profile_picture',
			'last_name',
			'first_name',
			'bio',
			'posts_count',
			'followers_count',
			'followings_count',
		)

	def get_profile_picture(self, user):
		picture_url = user.profile_user.profile_picture.url
		return self.context.get('request').build_absolute_uri(picture_url)

	def get_posts_count(self, user):
		posts_count = user.post_user.count()
		return posts_count

	def get_followers_count(self, user):
		followers_count = user.following.filter(pending=False).count()
		return followers_count

	def get_followings_count(self, user):
		followings_count = user.follower.filter(pending=False).count()
		return followings_count