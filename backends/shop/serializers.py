from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from shop.models import Shop, Product, Category


class ShopSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'url', 'state',)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'category',)
