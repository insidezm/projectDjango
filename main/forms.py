from django import forms
from .models import TextAn
from django.forms import ModelForm, Textarea, TextInput


class TextAnForm(forms.Form):
    class Meta:

        model = TextAn
        fields = ['title', 'full_text']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи',
            }),
            'full_name': Textarea(attrs={
                    'class': 'form-control',
                    'placeholder': 'Текст статьи'
            })
        }
