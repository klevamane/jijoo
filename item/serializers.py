from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from item.models import Item


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        read_only_fields = ("id",)

    def create(self, validated_data):
        item = Item(owner=self.context["request"].user, **validated_data)
        item.save()
        return item
