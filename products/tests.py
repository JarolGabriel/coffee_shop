from django.test import TestCase
from django.urls import reverse

from products.models import Product


class product_list(TestCase):
    def test_should_return_200(self):
        url = reverse("product_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content["products"].count(), 0)

    def test_should_return_200_with_product(self):
        url = reverse("product_list")
        Product.objects.create(
            name="test",
            description="test descriptiopn",
            price="5",
            available=True,
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content["products"].count(), 1)
