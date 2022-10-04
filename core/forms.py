from django import forms

from core.models import *


class ComponentAdd(forms.ModelForm):

    class Meta:
        model = Component
        fields = ['name', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
        }


class SupplierAdd(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = ['name', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
        }


