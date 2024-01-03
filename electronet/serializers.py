from rest_framework import serializers

from electronet.models import Product, Factory, Distributor, Businessman
from electronet.validators import FactoryOrDistributorValidator


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели "Продукт"
    """
    class Meta:
        model = Product
        fields = '__all__'


class BusinessmanSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели "Предприниматель"
    """
    class Meta:
        model = Businessman
        fields = '__all__'
        validators = [FactoryOrDistributorValidator(factory='factory', distributor='distributor')]
        read_only_fields = ('creation_date', 'debt',)


class DistributorSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели "Поставщик"
    """
    businessman = BusinessmanSerializer(source='businessman_set', many=True, read_only=True)

    class Meta:
        model = Distributor
        fields = ('name', 'email', 'country', 'city', 'street', 'building', 'distributor', 'product', 'debt',
                  'creation_date', 'businessman')
        read_only_fields = ('creation_date', 'debt', )


class FactorySerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели "Завод"
    """
    distributor = DistributorSerializer(source='distributor_set', many=True, read_only=True)
    businessman = BusinessmanSerializer(source='businessman_set', many=True, read_only=True)

    class Meta:
        model = Factory
        fields = ('name', 'email', 'country', 'city', 'street', 'building', 'product', 'creation_date',
                  'businessman', 'distributor')
