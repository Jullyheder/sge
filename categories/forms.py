from django.forms import (
    ModelForm,
    TextInput,
    Textarea
)
from categories.models import Category


class CategoryForm(ModelForm):

    class Meta:
        model = Category
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
