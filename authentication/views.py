from rest_framework import generics
from rest_framework.permissions import AllowAny

from authentication.serializers import SignupSerializer
from user.models import User


class SignupView(generics.CreateAPIView):
    """
    Allow a seller register a new account
    """

    queryset = User.objects.all()
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]
