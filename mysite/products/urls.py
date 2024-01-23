from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('new', views.product_create, name='product_new'),
]