from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Brand(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    brand_image_url = models.URLField(max_length=1024, null=True, blank=True)
    brand_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
         )
    brand = models.ForeignKey(
        'Brand', null=True, blank=True, on_delete=models.SET_NULL
         )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.IntegerField(blank=True, null=True, default=0)
    discounted_price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
         )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    @property
    def discount_in_percentage(self):
        return f"{self.discount} %"

    @property
    def discounted_price(self):
        if self.price and self.discount:
            subtotal = (self.price-((self.price*self.discount)/100))
            return round(subtotal, 2)

        else:
            return None

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    Comment model class.

    """
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="revies"
        )
    rating = models.IntegerField(default=3)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews",
        default="admin")
    approved = models.BooleanField(default=False)

    # Order of comments on screen: Oldest first
    class Meta:
        ordering = ['created_on']

    # Title String Function
    def __str__(self):
        return f"Comment {self.body} by {self.created_by}"
