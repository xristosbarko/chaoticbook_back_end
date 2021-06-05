from django.urls import path

from .views import (
    FollowAcceptOrDecline,
    FollowCreate,
    FollowDelete,
    FollowersList,
    FollowingsList,
)

app_name = "follows"

urlpatterns = [
    path("getFollowings", FollowingsList.as_view()),
    path("getFollowers", FollowersList.as_view()),
    path("create", FollowCreate.as_view()),
    path("delete/<user_id>", FollowDelete.as_view()),
    path("accept_or_decline/<user_id>", FollowAcceptOrDecline.as_view()),
]
