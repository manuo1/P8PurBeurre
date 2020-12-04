from django import forms

class ProductSearchForm(forms.Form):
    search = forms.CharField(label='Recherche', max_length=100)
