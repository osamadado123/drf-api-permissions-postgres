from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Snack


# Create your tests here.
class SnackTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = get_user_model().objects.create_user(
            username="test_user1", password="pass"
        )
        test_user1.save()

        test_user2 = get_user_model().objects.create_user(
            username="test_user2", password="pass"
        )
        test_user1.save()

        test_snack = Snack.objects.create(
            name="test_snack",
            purchaser=test_user1,
            desc="testing snack.",
        )
        test_snack.save()

    def setUp(self):
        self.client.login(username='test_user1', password="pass")

    def test_snacks_model(self):
        snack = Snack.objects.get(id=1)
        actual_purchaser = str(snack.purchaser)
        actual_name = str(snack.name)
        actual_description = str(snack.desc)
        self.assertEqual(actual_purchaser, "test_user1")
        self.assertEqual(actual_name, "test_snack")
        self.assertEqual(
            actual_description, "testing snack."
        )

    def test_get_snacks_list(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        snacks = response.data
        self.assertEqual(len(snacks), 1)
        self.assertEqual(snacks[0]["name"], "test_snack")

    def test_auth_required(self):
        self.client.logout()
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_purchaser_can_delete(self):
        self.client.logout()
        self.client.login(username='test_user2', password="pass")
        url = reverse("snack_detail", args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)