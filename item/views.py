from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from item.models import Item
from item.serializers import (
    ItemCreateSerializer,
    ItemListSerializer,
    ItemRetreiveSerializer,
)
from jijoo.utils import IsOwner


class ItemListView(generics.ListAPIView):
    serializer_class = ItemListSerializer
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()

    def list(self, request, *args, **kwargs):
        items = Item.objects.filter(owner=self.request.user)
        serializer = self.serializer_class(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ItemCreateView(generics.CreateAPIView):
    serializer_class = ItemCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()


class ItemDetailView(generics.RetrieveAPIView):
    serializer_class = ItemRetreiveSerializer
    permission_classes = [AllowAny]
    queryset = Item.objects.all()


class ItemDeleteView(generics.DestroyAPIView):
    serializer_class = ItemRetreiveSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Item.objects.all()
