from django.urls import path

from .views import ProfileCreate, ProfileDetails, ProfileEdit, getUserProfile

app_name = "profiles"

urlpatterns = [
    path("get", ProfileDetails.as_view()),
    path("create", ProfileCreate.as_view()),
    path("edit", ProfileEdit.as_view()),
    path("getUserProfile", getUserProfile.as_view()),
]
