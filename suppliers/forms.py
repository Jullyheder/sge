from django.forms import (
    ModelForm,
    TextInput,
    Textarea
)
from suppliers.models import Supplier


class SupplierForm(ModelForm):

    class Meta:
        model = Supplier
        fields = ['name', 'description']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '3'
                }
            )
        }
        labels = {
            'name': 'Nome',
            'description': 'Descrição'
        }
