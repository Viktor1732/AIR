from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Airplane, Contact


class AddAirplaneForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Airplane
        fields = ['title', 'slug', 'content', 'photo', 'cat']
        widgets = {'title': forms.TextInput(attrs={'placeholder': 'Название'}),
                   'slug': forms.TextInput(attrs={'placeholder': 'Слаг'}),
                   'content': forms.Textarea(attrs={'class': 'form-text', 'placeholder': 'Текст статьи'}),
                   'photo': forms.FileInput(attrs={'class': 'form-photo'}),
                   }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError('Длина превышает 50 символов.')
        return title

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if len(slug) > 20:
            raise ValidationError('Длина превышает 20 символов.')
        return slug


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Имя'}))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'Повтор пароля'}))
    captch = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'captch')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Имя'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Пароль'}))
    captch = CaptchaField()


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Имя'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'cols': 50, 'rows': 10, 'class': 'form-text', 'placeholder': 'Сообщение'})
        }
