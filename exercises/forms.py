from django.forms import ModelForm
from django import forms
from exercises.models import Book, Publisher

class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = "__all__"

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())