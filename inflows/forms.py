from django.forms import (
    ModelForm,
    Textarea,
    Select,
    NumberInput
)
from inflows.models import Inflow


class InflowForm(ModelForm):

    class Meta:
        model = Inflow
        fields = [
            'supplier', 'product', 'quantity', 'description'
        ]
        widgets = {
            'supplier': Select(attrs={'class': 'form-control'}),
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
            'supplier': 'Fornecedor',
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição'
        }
