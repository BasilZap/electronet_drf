from rest_framework import viewsets

from electronet.models import Product, Factory, Distributor, Businessman
from electronet.permissions import IsActive
from electronet.serializers import ProductSerializer, FactorySerializer, DistributorSerializer, BusinessmanSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для модели "Продукт"
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    action_permissions = [IsActive]


class FactoryViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для модели "Завод"
    """
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    action_permissions = [IsActive]


class DistributorViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для модели "Поставщик"
    """
    queryset = Distributor.objects.select_related('distributor')
    serializer_class = DistributorSerializer
    action_permissions = [IsActive]


class BusinessmanViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для модели "Предприниматель"
    """
    queryset = Businessman.objects.select_related('distributor', 'factory')
    serializer_class = BusinessmanSerializer
    action_permissions = [IsActive]
