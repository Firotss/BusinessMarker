from urllib import request, response
from django.test import TestCase
from django.urls import reverse, resolve
from BusinessMarker.utils.test_mixins import TestMixin
from django.contrib.auth import authenticate, models
from django.contrib.messages.storage.fallback import FallbackStorage

class TestBaseViews(TestMixin, TestCase):

    def test_LOGIN_VIEW(self):
        response = self.client.get('/login_menu/')
        self.assertEqual(response.status_code, 200)

    def test_USER_SIGN_IN(self):
        user = authenticate(username = "test", password = "123456")
        self.assertTrue(user.is_authenticated)

    def test_USER_SIGN_IN_FAILED(self):
        user = authenticate(username = "test", password = "123")
        self.assertEqual(user, None)