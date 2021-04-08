from rest_framework import generics

from authentication.serializers import SignupSerializer
from user.models import User


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
