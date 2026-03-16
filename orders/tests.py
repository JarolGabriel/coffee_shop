from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class MyOrderViewTests(TestCase):
    def test_no_longged_user_should_redurect(self):
        url = reverse("my_order")
        response = self.client.get(url)
        self.assertEqual(response.url, "")

    def test_longged_user_should_redurect(self):
        url = reverse("my_order")
        user = get_user_model().objects.create(username="test")
        self.client.force_login(user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
