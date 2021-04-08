from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from item.models import Item


class ItemCreateSerializer(ModelSerializer):
    class Meta:
        model = Item
        read_only_fields = ("id",)
        exclude = ["owner"]

    def create(self, validated_data):
        return Item.objects.create(owner=self.context["request"].user, **validated_data)


class ItemListSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
