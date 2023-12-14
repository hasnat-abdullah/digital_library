from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.signup_url = reverse('core:authentication:v1:signup')
        self.login_url = reverse('core:authentication:v1:token_obtain_pair')

    def test_user_signup_and_login(self):
        # User Signup
        signup_data = {'first_name': 'firstuser', 'last_name': 'lastuser', 'email': 'testuser@example.com',
                       'password': 'testpassword'}
        response = self.client.post(self.signup_url, data=signup_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # User Login
        login_data = {'email': 'testuser@example.com', 'password': 'testpassword'}
        response = self.client.post(self.login_url, data=login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
