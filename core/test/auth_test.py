from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse
class mytest(APITestCase):
    def setUp(self):
        self.user=User.objects.create_user(
            username='sanjay',
            password='password'
        )
        self.login_url=reverse('login')
    
    def test_login_success(self):
        data={
            'username':'sanjay',
            'password':'password'
        }

        response=self.client.post(self.login_url,data)
        self.assertEqual(response.data['message'],'login successfull')
        self.assertEqual(response.status_code,status.HTTP_200_OK)