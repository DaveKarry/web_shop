from time import timezone

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from .models import *
from .forms import *


# Create your views here.

def index(request):
    return render(request, 'users/index.html')

def contact(request):
    return render(request, 'users/contact.html')

def about(request):
    return render(request, 'users/about.html')

def new_tovars(request):
    return render(request, 'shop/new_tovars.html')

def custom_logout(request):
    logout(request)
    return render(request, 'users/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            new_purchase = Users_purchase()
            allstatuse = Status.objects.order_by('name')
            for status in allstatuse:
                if status.name == "Текущий":
                    new_purchase.create(user, status)
            login(request,user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request,'registration/register.html', context)

def catalog(request):
    tovars = Tovar.objects.order_by('price')
    return render(request, 'shop/catalog.html',{'tovars':tovars})

def create_tovar(request):
    if request.method == "POST":
        form =TovarForm(request.POST)
        if form.is_valid():
            tovar = form.save(commit=False)
            tovar.creation_time = timezone.now()
            tovar.save()
            return redirect('catalog')
    else:
        form = TovarForm()
        context = {'form': form}
        return render(request, 'shop/create_tovar.html', context)
