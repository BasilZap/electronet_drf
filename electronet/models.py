from django.core.exceptions import ValidationError
from django.utils import timezone

from django.db import models

from users.models import NULLABLE


# Модель "Продукт"
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название продукта')
    model = models.CharField(max_length=100, verbose_name='Модель продукта')
    launch_date = models.DateTimeField(verbose_name='Дата выхода на рынок')

    def __str__(self):
        return f'Продукт - {self.name} {self.model} (дата выхода - {self.model}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


# Модель "Завод"
class Factory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название завода')
    email = models.EmailField(verbose_name='Электронная почта')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    building = models.IntegerField(verbose_name='Номер дома')
    product = models.ManyToManyField(Product, verbose_name='Продукт', **NULLABLE)
    creation_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания', **NULLABLE)

    def __str__(self):
        return f'Завод - {self.name}'

    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'


# Модель "Поставщик"
class Distributor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название поставщика')
    email = models.EmailField(verbose_name='Электронная почта')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    building = models.IntegerField(verbose_name='Номер дома')
    product = models.ManyToManyField(Product, verbose_name='Продукт')
    distributor = models.ForeignKey(Factory, default=None, on_delete=models.DO_NOTHING, verbose_name='Поставщик',
                                    **NULLABLE)
    debt = models.FloatField(default=0.0, verbose_name='Задолженность')
    creation_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания', **NULLABLE)

    def __str__(self):
        return f'Компания - {self.name}, задолженность поставщику {self.distributor} - {self.debt}'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


# Модель "Предприниматель"
class Businessman(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название ИП')
    email = models.EmailField(verbose_name='Электронная почта')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    building = models.IntegerField(verbose_name='Номер дома')
    product = models.ManyToManyField(Product, verbose_name='Продукт')
    factory = models.ForeignKey(Factory, default=None, on_delete=models.DO_NOTHING, verbose_name='Завод',
                                **NULLABLE)
    distributor = models.ForeignKey(Distributor, default=None, on_delete=models.DO_NOTHING, verbose_name='Поставщик',
                                    **NULLABLE)
    debt = models.FloatField(default=0.0, verbose_name='Задолженность')
    creation_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания', **NULLABLE)

    def clean(self):
        """
        Валидация выбора поставщика в панели администратора
        :return:
        """
        if self.distributor and self.factory:
            raise ValidationError('Предприниматель может работать только с поставщиком или заводом')

    def __str__(self):
        return f'Предприниматель - {self.name}(ИД - {self.pk}), задолженность поставщику {self.distributor} - ' \
               f'{self.debt}'

    class Meta:
        verbose_name = 'Индивидуальный предприниматель'
        verbose_name_plural = 'Индивидуальные предприниматели'
