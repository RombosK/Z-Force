from django import forms
from .models import GiveHelp, GetHelp


# Форма анкеты волонтера
class GiveHelpForm(forms.ModelForm):
    agreement = forms.BooleanField(
        label='Согласие на обработку персональных данных', required=True)

    class Meta:
        model = GiveHelp
        fields = '__all__'


# Форма запроса на помощь
class GetHelpForm(forms.ModelForm):
    agreement = forms.BooleanField(
        label='Согласие на обработку персональных данных', required=True)

    class Meta:
        model = GetHelp
        # fields = '__all__'
        fields = ['name', 'surname', 'city',
                  'email', 'phone', 'text', ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'getHelp_input'}),
            'surname': forms.TextInput(attrs={'class': 'getHelp_input'}),
            'city': forms.TextInput(attrs={'class': 'getHelp_input'}),
            'email': forms.TextInput(attrs={'class': 'getHelp_input'}),
            'phone': forms.TextInput(attrs={'class': 'getHelp_input', 'placeholder': '+7(___)___-__-__'}),
            'text': forms.Textarea(attrs={'class': 'getHelp_inputTextArea', 'rows': 10}),
            # 'agreed': forms.CheckboxInput(attrs={'class': 'getHelp_inputCheckbox'}),
        }
# , 'cols': 50, 'rows': 10
        # labels = {'name': "bvz"}
