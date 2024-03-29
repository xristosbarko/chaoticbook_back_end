from rest_framework import serializers

from Accounts.serializers import UserSerializer
from ChaoticBook.permissions import isFollowing
from Posts.models import Post

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(), write_only=True
    )

    class Meta:
        model = Comment
        fields = (
            "id",
            "user",
            "post",
            "text",
            "timestamp",
        )

    def create(self, validated_data):
        request = self.context.get("request")

        user = request.user
        following = validated_data["post"].user
        isFollowing(following, user)

        validated_data["user"] = user
        comment = Comment.objects.create(**validated_data)

        return comment
