from django import forms
from .models import Product
from django.utils import timezone


class InStockToDiscard(forms.Form):
    count = forms.IntegerField()
    
    count.widget.attrs.update({'class' : 'form-control'})
    
    def save(self):
       pass
            
        
