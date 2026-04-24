from rest_framework.serializers import ModelSerializer
from products.models import Product


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id', 'title', 'brand', 'category', 'description',
            'serie_number', 'cost_price', 'selling_price', 'quantity'
        ]
