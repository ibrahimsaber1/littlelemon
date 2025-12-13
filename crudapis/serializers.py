from rest_framework import serializers
from .models import MenuItem


# 1- serializers
class menuItemSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    inventory = serializers.IntegerField()

# 2- ModelSerializer
class MenuItemModelSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    class Meta:
        model = MenuItem
        fields = ['id', 'title','price','stock']