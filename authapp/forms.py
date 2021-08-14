from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm, UserChangeForm


from authapp.models import ShopUser

from django.utils.translation import gettext_lazy as _


class ShopAuthenticationForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'forminput {field_name}'
            field.widget.attrs['placeholder'] = field_name


class ShopRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'email', 'password1', 'password2', 'photo', 'age')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'forminputreg {field_name}'
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Регистрация c 18 лет")
        return data


class ShopUserProfileForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'forminput {field_name}'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Регистрация c 18 лет")
        return data
