from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from network.models import NetworkUnit, Product

@admin.action(description="Обнуление задолженности")
def reset_debt(modeladmin, request, queryset):
    """Очищает задолженность у выбранных объектов"""
    queryset.update(debt=0)

@admin.register(NetworkUnit)
class NetworkUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'level', 'email', 'country', 'city', 'supplier_link', 'debt', 'date_create')
    list_filter = ('city', 'type', 'level')
    search_fields = ('name', 'email', 'country', 'city')
    actions = [reset_debt]

    def supplier_link(self, obj):
        if obj.supplier:
            url = reverse("admin:network_networkunit_change", args=[obj.supplier.id])
            return format_html(f'<a href="{url}">{obj.supplier.name}</a>')
        return "-"
    supplier_link.short_description = 'Поставщик'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'network_unit')
    list_filter = ('name', 'network_unit')
    search_fields = ('name', 'model')
    list_display_links = ('name',)