from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register',views.register, name='register'),
    path('custom_logout',views.custom_logout, name='logout'),
    path('catalog',views.catalog, name='catalog'),
    path('new_tovars',views.new_tovars, name='new_tovars'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('create_tovar',views.create_tovar, name='create_tovar')
]
