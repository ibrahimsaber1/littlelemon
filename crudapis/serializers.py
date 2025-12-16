from rest_framework import serializers
from .models import MenuItem, Category
from decimal import Decimal


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


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
    category = CategorySerializer()
    class Meta:
        model = MenuItem
        fields = ['id','category', 'title','price','stock','price_after_tax']
        depth = 1
        
    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)
    

class MenuItemModelSerializerCreate(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    category = CategorySerializer # will return the id of the category only
    class Meta:
        model = MenuItem
        fields = ['id','category', 'title','price','stock','price_after_tax']
        
    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)

# 2.2
class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    # category = CategorySerializer()
    class Meta:
        model = MenuItem
        fields = ['id','title','price','stock', 'price_after_tax','category']
        depth = 1 # this will include all the data related to any model with the depth of  so it will take the data of the directlly relarted models
        
    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)
    