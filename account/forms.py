from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)


#  class SignUpForm(forms.Form):
#     name = forms.CharField( max_length=20, min_length=6, required=True,empty_value='username',help_text='6-20 characters.')
#     email = forms.EmailField(required=True)
#     password = forms.CharField(max_length=8, min_length='6', required=True, widget=forms.PasswordInput, empty_value='password', help_text='....')
    