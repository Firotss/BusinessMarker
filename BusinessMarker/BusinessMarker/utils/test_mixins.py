import json
import os
from django.contrib.auth.models import User
from django.core.management import call_command
from django.conf import settings
from django.test import RequestFactory, Client


class TestMixin:
    fixtures = [os.path.join(settings.FIXTURES_DIRS, "fixtures.json")]
    admin_user = "admin"
    regular_user = "test"
    client = Client()
    factory = RequestFactory()

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        call_command("loaddata", self.fixtures, verbosity = 0)
        
    
    def _get_test_user(self, is_superuser=False):
        user = User.objects.get(username=self.regular_user)
        if is_superuser:
            user = User.objects.get(username=self.admin_user)

        return user