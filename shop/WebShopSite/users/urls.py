from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register',views.register, name='register'),
    path('custom_logout',views.custom_logout, name='logout'),
    path('catalog',views.catalog, name='catalog'),
    path('new_tovars',views.new_tovars, name='new_tovars'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
]
