from django.db import models

from jijoo.utils import TimeStampMixin


class Item(TimeStampMixin):
    name = models.CharField(max_length=100)
    descriprion = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=9)
    owner = models.ForeignKey("user.User", on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to="item_image")

    def __str__(self):
        return "{}".format(self.name)
