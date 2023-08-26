from django.test import SimpleTestCase
from django.urls import reverse, resolve
from checkout.views import checkout, checkout_success


class TestUrls(SimpleTestCase):

    def test_checkout_url_resolves(self):
        url = reverse("checkout")
        print(resolve(url))
        self.assertEqual(resolve(url).func, checkout)

    def test_checkout_success_url_resolves(self):
        url = reverse("checkout_success", args=['1'])
        print(resolve(url))
        self.assertEqual(resolve(url).func, checkout_success)
