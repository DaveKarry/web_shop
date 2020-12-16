from time import timezone

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import  DetailView
from django.views.generic import  View
from django.core.exceptions import ObjectDoesNotExist
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
            login(request,user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request,'registration/register.html', context)

def catalog(request):
    tovars = Tovar.objects.order_by('price')
    return render(request, 'shop/catalog.html',{'tovars':tovars})

@login_required
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


@login_required
def add_to_curent_order(request, slug):
    tovar = get_object_or_404(Tovar,slug=slug)
    orderItem, created = OrderItem.objects.get_or_create(item=tovar, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, is_ordered=False)
    if order_qs.exists():
        current_order = order_qs[0]
        if current_order.tovars.filter(item__slug=tovar.slug).exists():
            orderItem.quantity +=1
            orderItem.save()
        else:
            current_order.tovars.add(orderItem)
    else:
        ordered_date = timezone.now()
        current_order =Order.objects.create(user=request.user, ordered_date=ordered_date)
        current_order.tovars.add(orderItem)
    return  redirect("tovar", slug=slug)


class TovarDetailView(DetailView):
    model = Tovar
    template_name = "tovar.html"


class OrderView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, is_ordered=False)
            context ={'object':order}
            return render(self.request, "order.html", context)
        except ObjectDoesNotExist:
            messages.error(self.request, "У вас нет заказов!")
            return redirect("/")

