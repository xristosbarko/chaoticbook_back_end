from rest_framework import serializers
from .models import Like
from Posts.models import Post
from ChaoticBook.permissions import isFollowing

class LikeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Like
		fields = (
			'id',
			'post',
		)

	def create(self, validated_data):
		request = self.context.get('request')

		user = request.user
		following = validated_data['post'].user
		isFollowing(following, user)

		validated_data['user'] = user
		like = Like.objects.create(**validated_data)

		return like

class LikePostSerializer(serializers.ModelSerializer):
	username = serializers.CharField(source='user.username')
	profile_picture = serializers.SerializerMethodField()

	class Meta:
		model = Like
		fields = (
			'id',
			'username',
			'profile_picture',
		)

	def get_profile_picture(self, like):
		picture_url = like.user.profile_user.profile_picture.url
		return self.context.get('request').build_absolute_uri(picture_url)