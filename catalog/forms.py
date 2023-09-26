from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        ext = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for i in ext:
            if i in cleaned_data:
                raise forms.ValidationError('Запрещенное слово')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        ext = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for i in ext:
            if i in cleaned_data:
                raise forms.ValidationError('Запрещенное слово')
        return cleaned_data
