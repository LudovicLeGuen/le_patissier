from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import (index, legal, terms_conditions, privacy_policy,
                        guarantee)


class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse("home")
        print(resolve(url))
        self.assertEqual(resolve(url).func, index)

    def test_terms_conditions_url_resolves(self):
        url = reverse("terms_conditions")
        print(resolve(url))
        self.assertEqual(resolve(url).func, terms_conditions)

    def test_privacy_policy_url_resolves(self):
        url = reverse("privacy_policy")
        print(resolve(url))
        self.assertEqual(resolve(url).func, privacy_policy)

    def test_legal_url_resolves(self):
        url = reverse("legal")
        print(resolve(url))
        self.assertEqual(resolve(url).func, legal)

    def test_guarantee_url_resolves(self):
        url = reverse("guarantee")
        print(resolve(url))
        self.assertEqual(resolve(url).func, guarantee)
