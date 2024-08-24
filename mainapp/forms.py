from django import forms
from .models import GiveHelp, GetHelp


# Форма анкеты волонтера
class GiveHelpForm(forms.ModelForm):
    agreement = forms.BooleanField(
        label='Согласие на обработку персональных данных', required=True)

    class Meta:
        model = GiveHelp
        # fields = '__all__'
        fields = ['first_name', 'last_name', 'city',
                  'email', 'phone', 'text_1', 'text_2',
                  'schedule', 'help', 'mobility']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'volounteerFormWrapper__input'}),
            # 'first_name': forms.label(attrs={'class': 'volounteerFormWrapper__sign'}),
            'last_name': forms.TextInput(attrs={'class': 'volounteerFormWrapper__input'}),
            'city': forms.TextInput(attrs={'class': 'volounteerFormWrapper__input'}),
            'phone': forms.TextInput(attrs={'class': 'volounteerFormWrapper__input', 'placeholder': '+7(___)___-__-__'}),
            'email': forms.TextInput(attrs={'class': 'volounteerFormWrapper__input'}),
            'text_1': forms.Textarea(attrs={'class': 'getHelp_inputTextArea volounteerFormWrapper__textArea', 'rows': 8}),
            'text_2': forms.Textarea(attrs={'class': 'getHelp_inputTextArea volounteerFormWrapper__textArea', 'rows': 8}),
            'schedule': forms.Select(attrs={'class': 'volounteerFormWrapper__input'}),
            'help': forms.Select(attrs={'class': 'volounteerFormWrapper__input'}),
            'mobility': forms.Select(attrs={'class': 'volounteerFormWrapper__input'}),
        }


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
        }
