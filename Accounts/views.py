from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode
from django.views import View
from rest_framework import filters, generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import AuthSerializer, UserWithFollowSerializer
from .verification import account_activation_token


class ClientList(generics.ListAPIView):
    """
    Returns a list of all the Users.
    """

    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserWithFollowSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["username"]


class ClientCreate(generics.CreateAPIView):
    """
    Register a User.
    """

    serializer_class = AuthSerializer


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {"token": token.key, "user_id": user.pk, "username": user.username}
        )


class EmailVerification(View):
    def get(self, request, *args, **kwargs):
        uidb64 = self.kwargs["uidb64"]
        token = self.kwargs["token"]
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(
            user, token
        ):
            user.is_active = True
            user.save()
            return "Thank you for your email confirmation."
        else:
            return "Activation link is invalid!"
