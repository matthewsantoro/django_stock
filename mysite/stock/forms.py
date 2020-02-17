from django import forms
from .models import Product
from django.utils import timezone


class InStockToDiscard(forms.Form):
    title = forms.CharField(max_length=200)
    count = forms.IntegerField()

    title.widget.attrs.update({'class' : 'form-control'})
    count.widget.attrs.update({'class' : 'form-control'})
    
    def save(self):
       pass
            
        
