from django.urls import path

from .views import ClientCreate, ClientList, CustomAuthToken

app_name = "accounts"

urlpatterns = [
    path("login", CustomAuthToken.as_view()),
    path("register", ClientCreate.as_view()),
    path("search", ClientList.as_view()),
]
