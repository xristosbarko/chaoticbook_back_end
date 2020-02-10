from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from .serializers import CommentSerializer
from .models import Comment
from Posts.models import Post
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from ChaoticBook.permissions import isFollowing

class CommentCreate(generics.CreateAPIView):
	"""
	Add a Comment.
	"""
	permission_classes = [IsAuthenticated]
	serializer_class = CommentSerializer


class CommentDelete(generics.DestroyAPIView):
	"""
	Delete a Comment.
	"""
	permission_classes = [IsAuthenticated]
	serializer_class = CommentSerializer

	def get_queryset(self):
		user = self.request.user
		comment_id = self.kwargs['pk']

		comment = get_object_or_404(Comment, id=comment_id)

		if user == comment.user:
			return comment.delete()
		else:
			raise PermissionDenied(detail='You are not allowed to delete this comment.')

class getPostCommentsList(generics.ListAPIView):
	"""
	Returns a list of all the Posts.
	"""
	permission_classes = [IsAuthenticated]
	serializer_class = CommentSerializer

	def get_queryset(self):
		user = self.request.user
		post_id = self.kwargs['post_id']

		post = get_object_or_404(Post, id=post_id)

		following = post.user
		isFollowing(following, user)

		queryset = Comment.objects.filter(post=post).order_by('-timestamp')
		return queryset
