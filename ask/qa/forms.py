from django.core.exceptions import ValidationError
from django.forms.fields import CharField, EmailField
from django.forms.models import ModelForm
from django.forms.widgets import TextInput, Textarea, HiddenInput, PasswordInput
from django.contrib.auth.forms import AuthenticationForm
from django.forms import Form
from django.contrib.auth.models import User
from .models import Answer, Question


class AskForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text', 'author']
        widgets = {
            'title': TextInput(attrs={
                "class": "form__title",
            }),
            'text': Textarea(attrs={
                "class": "form__text"
            }),
            'author': HiddenInput(),
        }


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question', 'author']
        widgets = {
            'text': Textarea(attrs={
                "class": "form__text",
            }),
            'question': HiddenInput(),
            'author': HiddenInput(),
        }


class SignupForm(Form):
    username = CharField(label='Enter Username', min_length=4, max_length=150)
    email = EmailField(label='Enter email')
    password = CharField(label='Enter password', widget=PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return password

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password']
        )
        return user


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
