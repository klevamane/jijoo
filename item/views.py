from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from item.models import Item
from item.serializers import (
    InterestSerializer,
    ItemCreateSerializer,
    ItemListSerializer,
    ItemRetreiveSerializer,
)
from jijoo.utils import IsOwner


class BuyerItemsListView(generics.ListAPIView):
    """
    List Items posted by all sellers
    this view is visible anyone
    """

    serializer_class = ItemListSerializer
    permission_classes = [AllowAny]
    queryset = Item.objects.exclude(is_sold=True).order_by("-created_at")


class SellerItemsListView(generics.ListAPIView):
    """
    List Items posted by a particular seller
    this view is only visisble to the sell
    """

    serializer_class = ItemListSerializer
    queryset = Item.objects.all()

    def list(self, request, *args, **kwargs):
        items = Item.objects.filter(owner=self.request.user).order_by("-created_at")
        serializer = self.serializer_class(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SellerItemDetailsView(generics.RetrieveAPIView):
    serializer_class = ItemRetreiveSerializer
    permission_classes = [AllowAny]
    queryset = Item.objects.all()


class SellerItemCreateView(generics.CreateAPIView):
    """
    A seller should able to post a new item
    visible for everyone
    """

    serializer_class = ItemCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()


class SellerItemDeleteView(generics.DestroyAPIView):
    """
    A seller should able to delete an item
    posted by the seller
    """

    serializer_class = ItemRetreiveSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Item.objects.all()


class BuyerInterestCreateView(generics.CreateAPIView):
    """
    A buyer should able to indicate interest
    for an item posted by a seller
    """

    serializer_class = InterestSerializer
    permission_classes = [AllowAny]
    queryset = Item.objects.all()
