from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('register',Register.as_view(), name='register'),
    path('custom_logout',CustomLogout.as_view(), name='logout'),
    path('catalog',Catalog.as_view(), name='catalog'),
    path('about',About.as_view(), name='about'),
    path('contact',Contact.as_view(), name='contact'),
    path('create_tovar',CreateTover.as_view(), name='create_tovar'),
    path('tovar/<slug>/', TovarDetailView.as_view(), name='tovar'),
    path('order/', OrderView.as_view(), name='order'),
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('profile/', Profile.as_view(), name='profile'),
    path('add_address/', AddAddress.as_view(), name='add_address'),
    path('add_image/<slug>/', AddImage.as_view(), name='add_image'),
    path('add_email/', UpdateEmailView.as_view() , name='add_email'),
    path('make_order/', MakeOrder.as_view() , name='make_order'),
    path('delete/<slug>', DeleteTovar.as_view(), name='delete'),
    path('remove-from-order/<slug>/', RemoveFromOrder.as_view(), name='remove-from-order'),
    path('remove-item-from-order/<slug>', RemoveSingleItemFromOrder.as_view(), name='remove-single-item-from-order'),
    path('add-to-order/<slug>', AddToCurrentOrder.as_view(), name='add-to-order'),
    path('add-item-to-order/<slug>', AddSingleItemToOrder.as_view(), name='add-single-item-to-order'),
    #path('checkout/', CheckoutView.as_view(), name='checkout'),

]
