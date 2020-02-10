from django.urls import path
from .views import FollowingsList, FollowersList, FollowCreate, FollowDelete, FollowAcceptOrDecline

app_name = 'follows'

urlpatterns = [
	path('getFollowings', FollowingsList.as_view()),
	path('getFollowers', FollowersList.as_view()),
	path('create', FollowCreate.as_view()),
	path('delete/<user_id>', FollowDelete.as_view()),
	path('accept_or_decline/<user_id>', FollowAcceptOrDecline.as_view()),
]