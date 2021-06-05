from rest_framework import serializers

from Accounts.serializers import UserSerializer, UserWithFollowSerializer
from Likes.models import Like

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "picture",
            "description",
        )

    def create(self, validated_data):
        request = self.context.get("request")

        validated_data["user"] = request.user
        post = Post.objects.create(**validated_data)

        return post


class PostListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    liked = serializers.SerializerMethodField()
    liked_by_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "user",
            "title",
            "picture",
            "description",
            "liked",
            "liked_by_count",
            "timestamp",
        )

    def get_liked(self, post):
        request = self.context.get("request")
        likes = post.like_post.filter(user=request.user)

        if likes.count():
            return True
        else:
            return False

    def get_liked_by_count(self, post):
        likes_count = post.like_post.count()
        return likes_count


class UsersLikedSerializer(serializers.ModelSerializer):
    user = UserWithFollowSerializer()

    class Meta:
        model = Like
        fields = ("user",)

    def to_representation(self, like):
        representation = super(UsersLikedSerializer, self).to_representation(
            like
        )
        user_representation = representation.pop("user")
        for key in user_representation:
            representation[key] = user_representation[key]

        return representation
