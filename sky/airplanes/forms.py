from django import forms
from django.core.exceptions import ValidationError

from .models import Airplane


class AddAirplaneForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Airplane
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-input'}),
                   'content': forms.Textarea(attrs={'cols': 50, 'rows': 10})
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
