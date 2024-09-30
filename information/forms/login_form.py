from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=140, label='username')
    password = forms.CharField( label='password', widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username)<5:
            raise forms.ValidationError('Name must be longer than 5')
        return username