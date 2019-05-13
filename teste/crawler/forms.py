from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field
from .models import MarketplaceGoogle

class BuscaEan(forms.ModelForm):
    class Meta:
        model = MarketplaceGoogle
        fields = "__all__"

    helper = FormHelper()
    helper.form_class = 'form-group'
    helper.layout = Layout(
        Field('title', css_class='form-control mt-2 mb-3'),
        Field('text', rows="3", css_class='form-control mb-3'),
        Field('author', css_class='form-control mb-3'),
        Field('tags', css_class='form-control mb-3'),
        Field('slug', css_class='form-control'),
    )
    #ean = forms.CharField(max_length = 8, widget=forms.TextInput(attrs={'placeholder':'EAN','required': True,'class': 'form-control'}), required=True)

