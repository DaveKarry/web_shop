from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('register',register, name='register'),
    path('custom_logout',custom_logout, name='logout'),
    path('catalog',catalog, name='catalog'),
    path('new_tovars',new_tovars, name='new_tovars'),
    path('about',about, name='about'),
    path('contact',contact, name='contact'),
    path('create_tovar',create_tovar, name='create_tovar'),
    path('tovar/<slug>/', TovarDetailView.as_view(), name='tovar'),
    path('order/', OrderView.as_view(), name='order'),
    path('add-to-order/<slug>', add_to_curent_order, name='add-to-order'),
]
