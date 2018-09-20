from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Account

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        if Account.objects.email_exist(email):
            raise forms.ValidationError('Email already existed!')
        return email


class SignInForm(AuthenticationForm):
    pass

#  class SignUpForm(forms.Form):
#     name = forms.CharField( max_length=20, min_length=6, required=True,empty_value='username',help_text='6-20 characters.')
#     email = forms.EmailField(required=True)
#     password = forms.CharField(max_length=8, min_length='6', required=True, widget=forms.PasswordInput, empty_value='password', help_text='....')
    