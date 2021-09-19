from django.forms.widgets import HiddenInput
from .models import Answer, Question
from django.forms import ModelForm, TextInput, Textarea, ModelChoiceField


class AskForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text']
        widgets = {
            'title': TextInput(attrs={
                "class": "form__title",
            }),
            'text': Textarea(attrs={
                "class": "form__text"
            }),
        }


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question']
        widgets = {
            'text': Textarea(attrs={
                "class": "form__text",
            }),
            'question': HiddenInput(),
        }
