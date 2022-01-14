""" Form for use in creating new products """
from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """ Form for use in creating new products """
    class Meta:
        """ Uses Product Model as it's base and uses all fields """
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
