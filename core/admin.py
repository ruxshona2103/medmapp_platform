from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from solo.admin import SingletonModelAdmin
from adminsortable2.admin import SortableAdminMixin
from .models import SiteSettings, Specialty, Statistic, WorkStep, ServiceCard, Country, City


@admin.register(SiteSettings)
class SiteSettingsAdmin(SingletonModelAdmin):
    fieldsets = (
        ("Hero", {"fields": ("hero_title", "hero_subtitle", "hero_video")}),
        ("Contacts", {"fields": ("phone_number", "email", "address")}),
        ("Socials", {"fields": ("facebook_url", "instagram_url", "telegram_url", "youtube_url")}),
        ("SEO", {"fields": ("meta_title", "meta_description", "meta_keywords")}),
    )


@admin.register(Specialty)
class SpecialtyAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("title", "order")
    search_fields = ("title",)


@admin.register(Statistic)
class StatisticAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("title", "number", "order")


@admin.register(WorkStep)
class WorkStepAdmin(admin.ModelAdmin):
    list_display = ("step_number", "title")
    ordering = ("step_number",)


@admin.register(ServiceCard)
class ServiceCardAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("title", "order")


@admin.register(Country)
class CountryAdmin(TranslationAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(City)
class CityAdmin(TranslationAdmin):
    list_display = ("id", "name", "country")
    search_fields = ("name",)
    list_filter = ("country",)
