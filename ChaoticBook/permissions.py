from rest_framework.exceptions import PermissionDenied

from Follows.models import Follow


def isFollowing(following, user):
    if following != user:
        check_follow = Follow.objects.filter(
            following=following, follower=user, pending=False
        )
        if not check_follow:
            raise PermissionDenied(detail="You are not following this person.")
