from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from item.models import Interest, Item


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


class InterestSerializer(ModelSerializer):
    class Meta:
        model = Interest
        fields = ["name", "email", "location", "mobile"]


class CreateInterestSerializer(ModelSerializer):
    class Meta:
        model = Interest
        fields = ["id", "item", "name", "email", "location"]


class ItemRetreiveSerializer(ModelSerializer):
    interests = InterestSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ["id", "name", "description", "price", "interests"]
