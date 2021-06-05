from django.urls import path

from .views import LikeCreate, LikeDelete

app_name = "likes"

urlpatterns = [
    path("create", LikeCreate.as_view()),
    path("delete/<post_id>", LikeDelete.as_view()),
]
