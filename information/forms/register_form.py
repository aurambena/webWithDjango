from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(max_length=140, label='name')
    email = forms.EmailField(label='email')
    coment = forms.CharField(max_length=1000, label='coment', widget=forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name)<5:
            raise forms.ValidationError('Name must be longer than 5')
        return name