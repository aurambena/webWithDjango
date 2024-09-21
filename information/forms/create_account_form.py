from django import forms
from django.contrib.auth.password_validation import validate_password

class AccountForm(forms.Form):
    username = forms.CharField(max_length=140, label='user name')
    first_name = forms.CharField(max_length=140, label='first name')
    last_name = forms.CharField(max_length=140, label='last name')
    email = forms.EmailField(label='email')

    password1 =forms.CharField(widget=forms.PasswordInput(), label='Set your password')
    password2 =forms.CharField(widget=forms.PasswordInput(), label='Repeat your password')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2 and password1 != '':
            raise forms.ValidationError(('The passwords does not match'))
        
        if password2 != '':
            validate_password(password2)

        return password2
        


    