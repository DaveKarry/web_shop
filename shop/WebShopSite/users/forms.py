from django import forms
from .models import Tovar


class TovarForm(forms.ModelForm):
    class Meta:
        model = Tovar
        fields = ('name','image','count','short_description',
                  'full_description', 'price', 'category')