from django.forms import (
    ModelForm,
    Select,
    Textarea,
    NumberInput
)
from django.core.exceptions import ValidationError
from outflows.models import Outflow


class OutflowForm(ModelForm):

    class Meta:
        model = Outflow
        fields = ['product', 'quantity', 'description']
        widgets = {
            'product': Select(attrs={'class': 'form-control'}),
            'quantity': NumberInput(attrs={'class': 'form-control'}),
            'description': Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '3'
                }
            )
        }
        labels = {
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição'
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

        if quantity > product.quantity:
            raise ValidationError(
                'A Quantidade disponível em estoque para o produto '
                f'{product.title} é de {product.quantity} unidades.'
            )
        return quantity
