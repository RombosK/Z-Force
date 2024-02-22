from django import forms
from .models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['first_name', 'last_name', 'city', 'email', 'phone', 'text']


