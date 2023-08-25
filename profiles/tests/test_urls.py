from django.test import SimpleTestCase
from django.urls import reverse, resolve
from profiles.views import profile, order_history


class TestUrls(SimpleTestCase):

    def test_profile_url_resolves(self):
        url = reverse("profile")
        print(resolve(url))
        self.assertEqual(resolve(url).func, profile)

    def test_order_history_url_resolves(self):
        url = reverse("order_history", args=['1'])
        print(resolve(url))
        self.assertEqual(resolve(url).func, order_history)
