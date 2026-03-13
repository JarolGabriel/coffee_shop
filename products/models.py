from django.db import models


class Product(models.Model):
    name = models.TextField(max_length=200, verbose_name="name")
    description = models.TextField(max_length=300, verbose_name="descrition")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Price", default=0
    )
    available = models.BooleanField(default=True, verbose_name="avalilable")
    photo = models.ImageField(
        upload_to="logos", null=True, blank=True, verbose_name="photo"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="create date")

    def __str__(self):
        return self.name
