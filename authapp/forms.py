from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'age',
            'avatar'
        )

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            raise ValidationError('Контент 18+')
        else:
            return age


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'age',
            'avatar'
        )

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            raise ValidationError('Контент 18+')
        else:
            return age
