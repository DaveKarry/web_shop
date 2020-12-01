from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register',views.register, name='register'),
    path('custom_logout',views.custom_logout, name='logout'),
]
