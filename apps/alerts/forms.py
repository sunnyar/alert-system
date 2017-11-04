from django import forms
from models import Alert


class SearchForm(forms.Form):
    search_text = forms.CharField()