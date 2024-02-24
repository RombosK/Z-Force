from django import forms
from .models import RequestCharity, RequestVolunteer


# Форма анкеты благотворителя
class RequestFormCharity(forms.ModelForm):
    class Meta:
        model = RequestCharity
        fields = ['company_name', 'first_name', 'last_name', 'city', 'email', 'phone', 'help', 'text']


# Форма анкеты волонтера
class RequestFormVolunteer(forms.ModelForm):
    class Meta:
        model = RequestVolunteer
        fields = ['company_name', 'first_name', 'last_name', 'city', 'email', 'phone', 'schedule', 'mobility', 'text']



