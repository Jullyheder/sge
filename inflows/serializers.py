from rest_framework.serializers import ModelSerializer
from inflows.models import Inflow


class InflowSerializer(ModelSerializer):

    class Meta:
        model = Inflow
        fields = ['id', 'supplier', 'product', 'quantity', 'description']
