from django import forms
from .models import GiveHelp, GetHelp


# Форма анкеты волонтера
class GiveHelpForm(forms.ModelForm):
    agreement = forms.BooleanField(
        label='Согласие на обработку персональных данных', required=True)

    class Meta:
        model = GiveHelp
        fields = '__all__'

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
            # 'agreed': forms.CheckboxInput(attrs={'class': 'getHelp_inputCheckbox'}),
        }


# first_name = models.CharField(verbose_name='Имя', max_length=100)
#     last_name = models.CharField(verbose_name='Фамилия', max_length=100)
#     city = models.CharField(verbose_name='Город проживания', max_length=100)
#     email = models.EmailField(verbose_name='Электронная почта', unique=True)
#     phone = models.CharField(verbose_name='Телефон', max_length=20,
#                              validators=[validate_phone])
#     text_1 = models.TextField(verbose_name='Немного о себе')
#     text_2 = models.TextField(verbose_name='Как я хочу помочь')

#     schedule = models.CharField(verbose_name='сколько времени в неделю готовы уделять', choices=SCHEDULE, max_length=64,
#                                 blank=True)
#     help = models.CharField(verbose_name='варианты помощи', choices=HELP, max_length=64, blank=True)
#     mobility = models.CharField(verbose_name='мобильность', choices=MOBILITY, max_length=64, blank=True)


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
