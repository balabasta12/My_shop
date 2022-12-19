from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.http import JsonResponse
from requests import get
from rest_framework.response import Response
from rest_framework.views import APIView
from shop.models import (Category, Parameter, Product, ProductInfo,
                         ProductParameter, Shop, OrderItem, Order, Contact)
from shop.serializers import (CategorySerializer, ContactSerializer,
                              OrderSerializer, ParameterSerializer,
                              ProductInfoSerializer, ProductListSerializer,
                              ProductParameterSerializer, ShopSerializer, )
from yaml import Loader
from yaml import load as load_yaml

# Загрузка файла yaml


class PartnerUpdate(APIView):
    """
    Класс для обновления прайса от поставщика
    """
    def post(self, request, *args, **kwargs):
        # if not request.user.is_authenticated:
        #     return JsonResponse({'Status': False, 'Error': 'Log in required'}, status=403)
        #
        # if request.user.type != 'shop':
        #     return JsonResponse({'Status': False, 'Error': 'Только для магазинов'}, status=403)

        url = request.data.get('url')
        print(url)
        if url:
            validate_url = URLValidator()
            try:
                validate_url(url)
            except ValidationError as e:
                return JsonResponse({'Status': False, 'Error': str(e)})
            else:
                stream = get(url).content
                data = load_yaml(stream, Loader=Loader)
                print(data)

                shop, _ = Shop.objects.get_or_create(name=data['shop'], user_id=request.user.id)
                for category in data['categories']:
                    category_object, _ = Category.objects.get_or_create(id=category['id'], name=category['name'])
                    category_object.shops.add(shop.id)
                    category_object.save()
                ProductInfo.objects.filter(shop_id=shop.id).delete()
                for item in data['goods']:
                    product, _ = Product.objects.get_or_create(name=item['name'], category_id=item['category'])

                    product_info = ProductInfo.objects.create(product_id=product.id,
                                                              external_id=item['id'],
                                                              model=item['model'],
                                                              price=item['price'],
                                                              price_rrc=item['price_rrc'],
                                                              quantity=item['quantity'],
                                                              shop_id=shop.id)
                    for name, value in item['parameters'].items():
                        parameter_object, _ = Parameter.objects.get_or_create(name=name)
                        ProductParameter.objects.create(product_info_id=product_info.id,
                                                        parameter_id=parameter_object.id,
                                                        value=value)

                return JsonResponse({'Status': True})

        return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})


class Autorization(APIView):
    pass


class Registration(APIView):
    pass


class ShopView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Shop.objects.all()
        serializer = ShopSerializer(queryset, many=True)
        return Response(serializer.data)


class CategoryView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Category.objects.all()
        serializer = CategorySerializer
        return Response(serializer.data)


class ProductListView(APIView):
    def get (self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serializer = ProductListSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductInfoView(APIView):
    def get(self, request):
        queryset = ProductInfo.objects.all()
        serializer = ProductInfoSerializer(queryset, many=True)
        return Response(serializer.data)


class ParameterView(APIView):
    def get(self, request):
        queryset = Parameter.objects.all()
        serializer = ParameterSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductParameterView(APIView):
    def get(self, request):
        queryset = ProductParameter.objects.all()
        serializer = ProductParameterSerializer(queryset, many=True)
        return Response(serializer.data)


class OrderView(APIView):
    def get(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)


class OrderItemView(APIView):
    def get(self, request):
        queryset = OrderItem.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)


class ContactView(APIView):
    def get(self, request):
        queryset = Contact.objects.all()
        serializer = ContactSerializer(queryset, many=True)
        return Response(serializer.data)