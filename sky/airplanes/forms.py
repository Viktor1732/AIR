from django import forms

from .models import Airplane


class AddAirplaneForm(forms.ModelForm):
    class Meta:
        model = Airplane
        fields = ['title', 'slug', 'content', 'is_published', 'cat']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-input'}),
                   'content': forms.Textarea(attrs={'cols': 50, 'rows': 10})
                   }
