from django.db import models

from jijoo.utils import TimeStampMixin, validate_ng_mobile_number


def upload_image(instance, filename):
    return "images/{}/{}".format(instance.owner.id, filename)


class Item(TimeStampMixin):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=9)
    owner = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name="items"
    )
    image = models.ImageField(blank=True, null=True, upload_to=upload_image)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.name)


class Interest(TimeStampMixin):
    item = models.ForeignKey(
        "item.Item", on_delete=models.CASCADE, related_name="interests"
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    location = models.CharField(max_length=200)
    mobile = models.CharField(
        max_length=20, blank=True, null=True, validators=[validate_ng_mobile_number]
    )
