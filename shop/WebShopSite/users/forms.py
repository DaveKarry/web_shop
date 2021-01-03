from django import forms
from .models import Tovar, Adress, Order



class TovarForm(forms.ModelForm):
    class Meta:
        model = Tovar
        fields = ('name','image','short_description', 'full_description', 'price', 'category', 'slug')

class AdressForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = ('country', 'city','street','number', 'index',)

class UsersUpdateEmailForm(forms.Form):
    email = forms.CharField()

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Tovar
        fields =('image',)

class SelectAddressForm(forms.ModelForm):
    class Meta:
        model = Order
        fields =('shipping_address',)

