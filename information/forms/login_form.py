from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=140, label='username')
    password = forms.CharField( label='password', widget=forms.PasswordInput())

    