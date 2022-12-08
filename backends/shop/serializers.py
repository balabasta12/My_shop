from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from shop.models import Shop


class ShopSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name')