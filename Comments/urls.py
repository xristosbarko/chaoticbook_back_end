from django.urls import path

from .views import CommentCreate, CommentDelete, getPostCommentsList

app_name = "comments"

urlpatterns = [
    path("create", CommentCreate.as_view()),
    path("delete/<pk>", CommentDelete.as_view()),
    path("getPostCommentsList/<post_id>", getPostCommentsList.as_view()),
]
