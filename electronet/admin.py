from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from electronet.models import Product, Factory, Distributor, Businessman


def linkify(field_name):
    """
    Преобразование значения внешнего ключа в ссылку
    При нажатии на ссылку, пользователь перенаправляется на
    страницу редактирования объекта
    """

    def _linkify(obj):
        linked_obj = getattr(obj, field_name)
        if linked_obj is None:
            return '-'
        # Получение атрибутов
        app_label = linked_obj._meta.app_label
        model_name = linked_obj._meta.model_name
        # формирование ссылки
        view_name = f'admin:{app_label}_{model_name}_change'
        link_url = reverse(view_name, args=[linked_obj.pk])
        return format_html('<a href="{}">{}</a>', link_url, linked_obj)

    # Устанавливаем название колонки
    _linkify.short_description = field_name
    return _linkify


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'launch_date')


@admin.register(Factory)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'street', 'building', 'creation_date')
    readonly_fields = ('creation_date',)
    list_filter = ('country',)


@admin.register(Distributor)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'street', 'building', linkify(field_name='distributor'), 'debt',
                    'creation_date')
    readonly_fields = ('creation_date',)
    list_filter = ('country',)
    actions = ['set_debt_null', ]

    @admin.action(description='Обнулить задолженность')
    def set_debt_null(self, request, queryset):
        updated = queryset.update(debt=0.0)
        if updated == 1:
            user_message = 'Запись обновлена'
        else:
            user_message = f'{updated} обновлено'
        self.message_user(request, user_message)


@admin.register(Businessman)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'street', 'building', linkify(field_name='factory'),
                    linkify(field_name='distributor'), 'debt',
                    'creation_date')
    readonly_fields = ('creation_date',)
    list_display_links = ('name',)
    list_filter = ('country',)
    actions = ['set_debt_null', ]

    @admin.action(description='Обнулить задолженность')
    def set_debt_null(self, request, queryset):
        updated = queryset.update(debt=0.0)
        if updated == 1:
            user_message = 'Запись обновлена'
        else:
            user_message = f'{updated} обновлено'
        self.message_user(request, user_message)
