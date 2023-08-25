from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import (all_products, product_detail, all_brands,
                            one_brand, add_product, edit_product,
                            delete_product)


class TestUrls(SimpleTestCase):

    def test_products_url_resolves(self):
        url = reverse("products")
        print(resolve(url))
        self.assertEqual(resolve(url).func, all_products)

    def test_one_brand_url_resolves(self):
        url = reverse("one_brand")
        print(resolve(url))
        self.assertEqual(resolve(url).func, one_brand)

    def test_all_brands_url_resolves(self):
        url = reverse("all_brands")
        print(resolve(url))
        self.assertEqual(resolve(url).func, all_brands)

    def test_add_product_url_resolves(self):
        url = reverse("add_product")
        print(resolve(url))
        self.assertEqual(resolve(url).func, add_product)

    def test_product_detail_url_resolves(self):
        url = reverse("product_detail", args=['11'])
        print(resolve(url))
        self.assertEqual(resolve(url).func, product_detail)

    def test_edit_product_url_resolves(self):
        url = reverse("edit_product", args=['11'])
        print(resolve(url))
        self.assertEqual(resolve(url).func, edit_product)

    def test_delete_product_url_resolves(self):
        url = reverse("delete_product", args=['11'])
        print(resolve(url))
        self.assertEqual(resolve(url).func, delete_product)
