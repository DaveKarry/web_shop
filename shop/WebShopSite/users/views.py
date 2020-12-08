from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Tovar
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
            login(request,user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request,'registration/register.html', context)

def catalog(request):
    tovars = Tovar.objects.order_by('price')
    return render(request, 'shop/catalog.html',{'tovars':tovars})
