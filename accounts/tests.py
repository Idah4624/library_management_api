from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import User


class RegistrationTests(APITestCase):

    def test_user_registration(self):

        data = {
            "username": "john",
            "email": "john@gmail.com",
            "password": "john12345",
            "role": "member"
        }

        response = self.client.post(
            "/api/accounts/register/",
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            User.objects.count(),
            1
        )