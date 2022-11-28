from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def get_fields(self):
        fields = super().get_fields()
        if self.instance:
            fields['user'].read_only = True
            fields['book'].read_only = True
            fields['plated_end_at'].read_only = True
        return fields