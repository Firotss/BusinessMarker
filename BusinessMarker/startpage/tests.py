from django.test import TestCase
from django.urls import reverse

class TestBaseViews(TestCase):

    def test_LOGIN_VIEW(self):
        response = self.client.get('/login_menu/')
        self.assertEqual(response.status_code, 200)