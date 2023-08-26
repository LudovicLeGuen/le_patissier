from django.test import TestCase, Client
from django.urls import reverse
from home.models import Contact
import json


class TestViews(TestCase):
