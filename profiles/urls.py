from django.urls import path
from . import views
from .views import DeleteMyProfile

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
    path("profile/delete-user/<int:pk>/",
         DeleteMyProfile.as_view(), name="delete-user"),
]
