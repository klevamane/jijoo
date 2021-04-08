from django.http import HttpResponseForbidden
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from item.models import Item
from item.serializers import ItemSerializer
from user.models import User


class ItemListCreateView(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        items = Item.objects.filter(owner=self.request.user)
        serializer = self.serializer_class(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def post(self, request, *args, **kwargs):
    #     return super(ItemListCreateView, self).create(request, *args, **kwargs)
