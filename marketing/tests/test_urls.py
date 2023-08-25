from django.test import SimpleTestCase
from django.urls import reverse, resolve
from marketing.views import (subscribe_view, subscribe_success_view,
                             subscribe_fail_view, unsubscribe_view,
                             unsubscribe_success_view, unsubscribe_fail_view,
                             mailchimp_ping_view)


class TestUrls(SimpleTestCase):

    def test_subscribe_view_url_resolves(self):
        url = reverse("subscribe")
        print(resolve(url))
        self.assertEqual(resolve(url).func, subscribe_view)

    def test_subscribe_success_view_url_resolves(self):
        url = reverse("subscribe-success")
        print(resolve(url))
        self.assertEqual(resolve(url).func, subscribe_success_view)

    def test_subscribe_fail_view_url_resolves(self):
        url = reverse("subscribe-fail")
        print(resolve(url))
        self.assertEqual(resolve(url).func, subscribe_fail_view)

    def test_unsubscribe_url_resolves(self):
        url = reverse("unsubscribe")
        print(resolve(url))
        self.assertEqual(resolve(url).func, unsubscribe_view)

    def test_unsubscribe_success_url_resolves(self):
        url = reverse("unsubscribe-success")
        print(resolve(url))
        self.assertEqual(resolve(url).func, unsubscribe_success_view)

    def test_unsubscribe_fail_url_resolves(self):
        url = reverse("unsubscribe-fail",)
        print(resolve(url))
        self.assertEqual(resolve(url).func, unsubscribe_fail_view)
