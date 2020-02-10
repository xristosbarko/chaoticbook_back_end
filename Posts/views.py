from .models import Post
from Follows.models import Follow
from Likes.models import Like
from .serializers import PostSerializer, PostListSerializer, UsersLikedSerializer
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from .filters import PostListFilter
from rest_framework.exceptions import PermissionDenied
from ChaoticBook.permissions import isFollowing
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination

class PostList(generics.ListAPIView):
	"""
	Returns a list of all the Posts.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Post.objects.all()
	pagination_class = PageNumberPagination
	pagination_class.page_size = 12
	serializer_class = PostListSerializer
	filter_backends = [PostListFilter]


class PostDetails(generics.RetrieveAPIView):
	"""
	Returns the details of a Post.
	"""
	permission_classes = [IsAuthenticated]
	serializer_class = PostSerializer

	def get_object(self):
		user = self.request.user
		post_id = self.kwargs['pk']

		post = get_object_or_404(Post, id=post_id)

		following = post.user
		isFollowing(following, user)

		return post


class PostCreate(generics.CreateAPIView):
	"""
	Add a Post.
	"""
	permission_classes = [IsAuthenticated]
	serializer_class = PostSerializer


class PostDelete(generics.DestroyAPIView):
	"""
	Delete a Post.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	def perform_destroy(self, instance):
		user = self.request.user

		if user == instance.user:
			return instance.delete()
		else:
			raise PermissionDenied(detail='You are not allowed to delete this post.')

class getFollowingsPosts(generics.ListAPIView):
	"""
	Returns the Posts of the users that are being followed.
	"""
	permission_classes = [IsAuthenticated]
	serializer_class = PostListSerializer

	def get_queryset(self):
		user = self.request.user

		followings = Follow.objects.filter(follower=user, pending=False).values_list('following', flat=True)
		users = list(followings)
		users.append(user.id)
		queryset = Post.objects.filter(user__in=users).order_by('-timestamp')

		return queryset

class getUsersLiked(generics.ListAPIView):
	"""
	Returns a list of all the users that like the post.
	"""
	permission_classes = [IsAuthenticated]
	serializer_class = UsersLikedSerializer

	def get_queryset(self):
		user = self.request.user

		post_id = self.kwargs['post_id']
		post = get_object_or_404(Post, id=post_id)
		following = post.user
		isFollowing(following, user)

		queryset = Like.objects.filter(post=post)

		return queryset