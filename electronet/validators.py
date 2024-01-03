from rest_framework.serializers import ValidationError


class FactoryOrDistributorValidator:
    """
    Валидатор для модели "Предприниматель"
    Запрет на выбор одновременно поставщика и завода
    """
    def __init__(self, factory, distributor):
        self.factory = factory
        self.distributor = distributor

    def __call__(self, values):
        factory = dict(values).get(self.factory)
        distributor = dict(values).get(self.distributor)

        if factory and distributor:
            raise ValidationError('Предприниматель может работать только с поставщиком или заводом')
