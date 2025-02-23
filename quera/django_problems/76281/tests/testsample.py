from account.forms import *
from account.models import *
from account.views import *
from django.test import Client, TestCase
from django.urls import reverse


class TestAll(TestCase):

    def test_login_success_redirect(self):
        Account.objects.create(username="test1", password="test1pass")
        account = Account.objects.get(username="test1")
        account.set_password("test1pass")
        account.save()
        response = self.client.post(reverse('login'), data={'username': 'test1', 'password': 'test1pass'})
        self.assertEqual(response.url, '/home/')