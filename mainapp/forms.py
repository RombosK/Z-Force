from django import forms
from .models import GiveHelp, GetHelp


# Форма анкеты волонтера
class GiveHelpForm(forms.ModelForm):
    class Meta:
        model = GiveHelp
        fields = '__all__'


# Форма запроса на помощь
class GetHelpForm(forms.ModelForm):
    class Meta:
        model = GetHelp
        fields = '__all__'




