from django import forms

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
