from django import forms
from .models import Bookshelf

class bookForm(forms.ModelForm):
    class Meta:
        model=Bookshelf
        fields= ['title','author','isbn','summary','genre',]
