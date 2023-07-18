from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('all_brands', views.all_brands, name='all_brands'),
    path('<product_id>', views.product_detail, name='product_detail'),

]
