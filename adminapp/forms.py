from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from authapp.forms import forms
from authapp.models import ShopUser
from mainapp.models import CategoryProduct, Product


class AdminShopUserCreateForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username', 'first_name', 'last_name', 'is_superuser',
            'is_staff', 'email', 'password1', 'password2', 'photo',
            'age',
        )

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


class AdminShopUserUpdateForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username', 'first_name', 'last_name', 'is_superuser',
            'is_staff', 'is_active', 'email', 'password', 'photo',
            'age',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'forminputreg {field_name}'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Регистрация c 18 лет")
        return data


class AdminProductCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = CategoryProduct
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'forminputreg1 {field_name}'


class AdminProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'forminputreg1 {field_name}'
