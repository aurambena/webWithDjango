from django import forms

class SearchForm(forms.Form):
    s = forms.CharField(
        label='Search',
        max_length=100,
    )
