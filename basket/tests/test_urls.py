from django.test import SimpleTestCase
from django.urls import reverse, resolve
from basket.views import (view_basket, add_to_basket, adjust_basket,
                          remove_from_basket)


class TestUrls(SimpleTestCase):

    def test_view_basket_url_resolves(self):
        url = reverse("view_basket")
        print(resolve(url))
        self.assertEqual(resolve(url).func, view_basket)

    def test_add_to_basket_url_resolves(self):
        url = reverse("add_to_basket", args=['1'])
        print(resolve(url))
        self.assertEqual(resolve(url).func, add_to_basket)

    def test_adjust_basket_url_resolves(self):
        url = reverse("adjust_basket", args=['1'])
        print(resolve(url))
        self.assertEqual(resolve(url).func, adjust_basket)

    def test_remove_from_basket_url_resolves(self):
        url = reverse("remove_from_basket", args=['1'])
        print(resolve(url))
        self.assertEqual(resolve(url).func, remove_from_basket)
