from rest_framework.serializers import ModelSerializer

from user.models import User


class SignupSerializer(ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ("id", "is_admin", "last_login")
        exclude = [
            "is_seller",
            "is_admin",
            "groups",
            "user_permissions",
            "is_superuser",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        # use this method so we can also has the user's password
        return User.objects.create_user(**validated_data)
