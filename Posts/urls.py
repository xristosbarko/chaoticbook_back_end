from django.urls import path
from .views import PostList, PostDetails, PostCreate, PostDelete, getFollowingsPosts, getUsersLiked

app_name = 'posts'

urlpatterns = [
	path('', PostList.as_view()),
	path('get/<pk>', PostDetails.as_view()),
	path('create', PostCreate.as_view()),
	path('delete/<pk>', PostDelete.as_view()),
	path('getFollowingsPosts', getFollowingsPosts.as_view()),
	path('getUsersLiked/<post_id>', getUsersLiked.as_view()),
]