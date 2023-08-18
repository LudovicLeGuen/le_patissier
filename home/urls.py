from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path("legal", views.legal, name="legal"),
    path("privacy_policy", views.privacy_policy, name="privacy_policy"),
    path("guarantee", views.guarantee, name="guarantee"),
    path("terms_conditions", views.terms_conditions, name="terms_conditions"),
    path("contact", views.contact, name="contact"),
]
