from rest_framework import serializers
from .models import MenuItem
from decimal import Decimal

# 1- serializers
class menuItemSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    inventory = serializers.IntegerField()

# 2- ModelSerializer
class MenuItemModelSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')

    class Meta:
        model = MenuItem
        fields = ['id', 'title','price','stock','price_after_tax']
        
    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)