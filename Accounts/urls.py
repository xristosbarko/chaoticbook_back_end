from django.urls import path
from .views import ClientCreate, CustomAuthToken, ClientList

app_name = 'accounts'

urlpatterns = [
	path('login', CustomAuthToken.as_view()),
	path('register', ClientCreate.as_view()),
	path('search', ClientList.as_view()),
]