from rest_framework import generics

from user.models import User
from user.serializers import UserSerializer


class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
