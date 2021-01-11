from django import forms

class ProductSearchForm(forms.Form):
    search = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(ProductSearchForm, self).__init__(*args, **kwargs)
        self.fields['search'].widget.attrs.update({'class': 'form-control'})
        self.fields['search'].widget.attrs.update({'placeholder': 'Chercher'})
