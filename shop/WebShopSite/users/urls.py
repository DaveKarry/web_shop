from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('register',register, name='register'),
    path('custom_logout',custom_logout, name='logout'),
    path('catalog',catalog, name='catalog'),
    path('about',about, name='about'),
    path('contact',contact, name='contact'),
    path('create_tovar',create_tovar, name='create_tovar'),
    path('tovar/<slug>/', TovarDetailView.as_view(), name='tovar'),
    path('order/', OrderView.as_view(), name='order'),
    path('checkout/', checkout, name='checkout'),
    path('profile/', profile, name='profile'),
    path('add_address/', add_address, name='add_address'),
    path('add_email/', UpdateEmailView.as_view() , name='add_email'),
    path('delete/<slug>', delete, name='delete'),
    path('remove-from-order/<slug>/', remove_from_order, name='remove-from-order'),
    path('remove-item-from-order/<slug>', remove_single_item_from_order, name='remove-single-item-from-order'),
    path('add-to-order/<slug>', add_to_curent_order, name='add-to-order'),
    path('add-item-to-order/<slug>', add_single_item_to_order, name='add-single-item-to-order'),
    #path('checkout/', CheckoutView.as_view(), name='checkout'),

]
