from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from shop.models import (Category, Contact, Order, OrderItem, Parameter,
                         Product, ProductInfo, ProductParameter, Shop, Us)

class UsSerializer(ModelSerializer):
    class Meta:
        model = Us
        fields = ('id', 'username', 'email',)


class ShopSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'url', 'filename',)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'shop', 'name',)


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'category',)


class ProductInfoSerializer(ModelSerializer):
    class Meta:
        model = ProductInfo
        fields = ('id', 'product', 'shop', 'name', 'quantity', 'price', 'price_rrc')


class ParameterSerializer(ModelSerializer):
    class Meta:
        model = Parameter
        fields = ('id', 'name')


class ProductParameterSerializer(ModelSerializer):
    class Meta:
        model = ProductParameter
        fields = ('id', 'product_info', 'parameter', 'value')


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'dt', 'status')


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product', 'shop', 'quantity')


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'type', 'user', 'value')