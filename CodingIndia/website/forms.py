from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from website.models import ContactUs, NewsLetter

class CreateUserForm(UserCreationForm):
    phone_no = forms.CharField(max_length = 10)
    class Meta:
        model = User
        fields = ["first_name","last_name", "username","email","phone_no","password1", 'password2']


class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"



class NewsLetterForm(ModelForm):
    class Meta:
        model = NewsLetter
        fields = "__all__"