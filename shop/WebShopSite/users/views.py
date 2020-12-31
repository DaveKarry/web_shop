from time import timezone

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  DetailView
from django.views.generic import  View
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import *
from .forms import *
import time


# Create your views here.

class Index(View):
    def get(self,*args, **kwargs):
        return render(self.request, 'users/index.html')

class Contact(View):
    def get(self,*args, **kwargs):
        return render(self.request, 'users/contact.html')

class About(View):
    def get(self,*args, **kwargs):
        return render(self.request, 'users/about.html')

class CustomLogout(View):
    def get(self,*args, **kwargs):
        logout(self.request)
        return render(self.request, 'users/index.html')

class DeleteTovar(View):
    def get(self, *args, **kwargs):
        print(kwargs)
        tovar = get_object_or_404(Tovar, slug=kwargs['slug'])
        tovar.delete()
        return redirect('catalog')

class Register(View):
    def get(self, *args, **kwargs):
        form = UserCreationForm()
        context = {'form': form}
        return render(self.request, 'registration/register.html', context)

    def post(self,*args, **kwargs):
        form = UserCreationForm(self.request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(self.request, user)
            time.sleep(1)
            return redirect('index')
        else:
            messages.info(self.request, 'Ошибка регистрации! Проверьте поля!')
            return HttpResponseRedirect('register')

class Catalog(View):
    def get(self,*args,**kwargs):
        tovars = Tovar.objects.order_by('price')
        return render(self.request, 'shop/catalog.html', {'tovars': tovars})

class CreateTover(View):
    @method_decorator(login_required)
    def get(self,*args,**kwargs):
        form = TovarForm()
        context = {'form': form}
        return render(self.request, 'shop/create_tovar.html', context)
    def post(self, *args,**kwargs):
        messages = False
        form = TovarForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog')
        else:
            messages.info(self.request, 'Какая-то ошибка! Прверьте поля или попробуйте снова!')
            return HttpResponseRedirect('create_tovar')

class AddToCurrentOrder(View):
    @method_decorator(login_required)
    def get(self,*args,**kwargs):
        tovar = get_object_or_404(Tovar, slug=kwargs['slug'])
        orderItem, created = OrderItem.objects.get_or_create(
            item=tovar,
            user=self.request.user,
            ordered=False)
        order_qs = Order.objects.filter(user=self.request.user, is_ordered=False)
        if order_qs.exists():
            current_order = order_qs[0]
            if current_order.tovars.filter(item__slug=tovar.slug).exists():
                orderItem.quantity += 1
                orderItem.save()
            else:
                current_order.tovars.add(orderItem)
        else:
            ordered_date = timezone.now()
            current_order = Order.objects.create(user=self.request.user, ordered_date=ordered_date)
            current_order.tovars.add(orderItem)
        return redirect("tovar", slug=kwargs['slug'])

class TovarDetailView(DetailView):
    model = Tovar
    template_name = "shop/tovar.html"

class OrderView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, is_ordered=False)
            context ={'object':order}
            return render(self.request, "order.html", context)
        except ObjectDoesNotExist:
            messages.error(self.request, "У вас нет заказов!")
            return redirect("/")

class RemoveFromOrder(View):
    @method_decorator(login_required)
    def get(self,*args, **kwargs):
        item = get_object_or_404(Tovar, slug=kwargs['slug'])
        order_qs = Order.objects.filter(
            user=self.request.user,
            is_ordered=False
        )
        if order_qs.exists():
            order = order_qs[0]
            # check if the order item is in the order
            if order.tovars.filter(item__slug=item.slug).exists():
                order_item = OrderItem.objects.filter(
                    item=item,
                    user=self.request.user,
                    ordered=False
                )[0]
                order.tovars.remove(order_item)
                order_item.delete()
                return redirect("order")
            else:
                return redirect("tovar", slug=kwargs['slug'])
        else:
            return redirect("tovar", slug=kwargs['slug'])

class RemoveSingleItemFromOrder(View):
    @method_decorator(login_required)
    def get(self, *args, **kwargs):
        item = get_object_or_404(Tovar, slug=kwargs['slug'])
        order_qs = Order.objects.filter(
            user=self.request.user,
            is_ordered=False
        )
        if order_qs.exists():
            order = order_qs[0]
            if order.tovars.filter(item__slug=item.slug).exists():
                order_item = OrderItem.objects.filter(
                    item=item,
                    user=self.request.user,
                    ordered=False
                )[0]
                if order_item.quantity > 1:
                    order_item.quantity -= 1
                    order_item.save()
                else:
                    order.tovars.remove(order_item)
                return redirect("order")
            else:
                return redirect("tovar", slug=kwargs['slug'])
        else:
            return redirect("tovar", slug=kwargs['slug'])

class AddSingleItemToOrder(View):
    @method_decorator(login_required)
    def get(self, *args, **kwargs):
        tovar = get_object_or_404(Tovar, slug=kwargs['slug'])
        order_qs = Order.objects.filter(
            user=self.request.user,
            is_ordered=False
        )
        if order_qs.exists:
            order = order_qs[0]
            if order.tovars.filter(item__slug=tovar.slug).exists():
                order_item = OrderItem.objects.filter(
                    item=tovar,
                    user=self.request.user,
                    ordered=False
                )[0]
                order_item.quantity += 1
                order_item.save()
                return redirect("order")
            else:
                return redirect("tovar", slug=kwargs['slug'])
        else:
            return redirect("tovar", slug=kwargs['slug'])

class Checkout(View):
    def get(self,*args,**kwargs):
        return render(self.request, 'users/checkout.html')

class Profile(View):
    def get(self, *args, **kwargs):
        addresses = Adress.objects.filter(
            user=self.request.user
        )
        context = {'addresses': addresses}
        return render(self.request, 'users/profile.html', context)

class AddAddress(View):
    def get(self, *args, **kwargs):
        form  = AdressForm()
        context = {
            'form': form
        }
        return render(self.request, 'users/add_address.html', context)
    def post(self, *args,**kwargs):
        form = AdressForm(self.request.POST or None)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = self.request.user
            form.save()
            return redirect('profile')
        else:
            return redirect('add_address')

class UpdateEmailView(View):
    def get(self, *args, **kwargs):
        form = UsersUpdateEmailForm()
        context = {
            'form': form
        }
        return render(self.request, 'users/add_email.html', context)
    def post(self,*args, **kwargs):
        form = UsersUpdateEmailForm(self.request.POST or None)
        if form.is_valid():
            user = self.request.user
            user.email = form.cleaned_data['email']
            user.save()
            return redirect('profile')
        else:
            return redirect('add_email')

class AddImage(View):
    def get(self,*args,**kwargs):
        form = ImageUploadForm()
        context = {
            'form' : form
        }
        return render(self.request, 'shop/add_image.html', context)
    def post(self,*args,**kwargs):
        form = ImageUploadForm(self.request.POST or None, self.request.FILES)
        if form.is_valid():
            tovar = Tovar.objects.get(slug=kwargs['slug'])
            tovar.image=form.cleaned_data['image']
            tovar.save()
            return redirect('tovar', slug=kwargs['slug'])
        else:
            messages.error(self.request, "Что-то опять пошло не так")
            return redirect('tovar', slug=kwargs['slug'])