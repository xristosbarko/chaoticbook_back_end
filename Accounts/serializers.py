from django.contrib.auth.models import User
from rest_framework import serializers

from Follows.models import Follow
from Profiles.models import Profile

# from .verification import sendVerificationEmail


class AuthSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(write_only=True)
    gender = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "last_name",
            "first_name",
            "birth_date",
            "gender",
            "email",
            "password",
        )

    def create(self, validated_data):
        # validated_data["is_active"] = False
        birth_date = validated_data.pop("birth_date")
        gender = validated_data.pop("gender")
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, birth_date=birth_date, gender=gender)
        # request = self.context.get('request')
        # sendVerificationEmail(request, user)

        return user


class UserSerializer(serializers.ModelSerializer):
    profile_picture = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "profile_picture",
        )

    def get_profile_picture(self, user):
        picture_url = user.profile_user.profile_picture.url
        return self.context.get("request").build_absolute_uri(picture_url)


class UserWithFollowSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source="id")
    profile_picture = serializers.SerializerMethodField()
    follow = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "user_id",
            "username",
            "profile_picture",
            "follow",
        )

    def get_profile_picture(self, user):
        picture_url = user.profile_user.profile_picture.url
        return self.context.get("request").build_absolute_uri(picture_url)

    def get_follow(self, user):
        request = self.context.get("request")
        check_follow = Follow.objects.filter(
            following=user, follower=request.user
        )
        if check_follow.count():
            return {"sent": True, "pending": check_follow[0].pending}
        else:
            return {"sent": False}

    def to_representation(self, user):
        representation = super(
            UserWithFollowSerializer, self
        ).to_representation(user)
        request = self.context.get("request")
        if user == request.user:
            representation.pop("follow")
        return representation
