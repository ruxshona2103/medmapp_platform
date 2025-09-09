from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Country, City, CounterStat, HowItWorksStep, ServiceCard


@admin.register(Country)
class CountryAdmin(TranslatableAdmin):
    list_display = ("__str__", "iso2", "order_index", "created_at")
    list_display_links = ("__str__",)
    list_editable = ("order_index",)
    search_fields = ("translations__name", "iso2")
    fieldsets = (
        ("Tarjima", {"fields": ("name", "slug")}),
        ("Umumiy", {"fields": ("iso2", "order_index")}),
    )


@admin.register(City)
class CityAdmin(TranslatableAdmin):
    list_display = ("__str__", "country", "order_index")
    list_display_links = ("__str__",)
    list_editable = ("order_index",)
    list_filter = ("country",)
    search_fields = ("translations__name", "country__translations__name")
    fieldsets = (
        ("Tarjima", {"fields": ("name", "slug")}),
        ("Umumiy", {"fields": ("country", "order_index")}),
    )


@admin.register(CounterStat)
class CounterStatAdmin(TranslatableAdmin):
    list_display = ("__str__", "value_int", "is_active", "order_index")
    list_display_links = ("__str__",)
    list_editable = ("value_int", "is_active", "order_index")
    search_fields = ("translations__label",)


@admin.register(HowItWorksStep)
class HowItWorksStepAdmin(TranslatableAdmin):
    list_display = ("order_index", "__str__", "is_active")
    list_display_links = ("__str__",)
    list_editable = ("order_index", "is_active")
    search_fields = ("translations__title",)


@admin.register(ServiceCard)
class ServiceCardAdmin(TranslatableAdmin):
    list_display = ("__str__", "is_active", "order_index")
    list_display_links = ("__str__",)
    list_editable = ("is_active", "order_index")
    search_fields = ("translations__title",)
