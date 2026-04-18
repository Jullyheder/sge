from django.forms import (
    ModelForm,
    TextInput,
    Textarea,
    Select,
    NumberInput
)
from products.models import Product


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = [
            'title', 'brand', 'category',
            'description', 'serie_number',
            'cost_price', 'selling_price',
        ]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'brand': Select(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'}),
            'description': Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '3'
                }
            ),
            'serie_number': TextInput(attrs={'class': 'form-control'}),
            'cost_price': NumberInput(attrs={'class': 'form-control'}),
            'selling_price': NumberInput(attrs={'class': 'form-control'})
        }
        labels = {
            'title': 'Título',
            'brand': 'Marca',
            'category': 'Categoria',
            'description': 'Descrição',
            'serie_number': 'Número de Série',
            'cost_price': 'Preço de Custo',
            'selling_price': 'Preço de Venda'
        }
