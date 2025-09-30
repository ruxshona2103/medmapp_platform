from modeltranslation.translator import register, TranslationOptions
from .models import SiteSettings, Specialty, Statistic, WorkStep, ServiceCard, Country, City


@register(SiteSettings)
class SiteSettingsTR(TranslationOptions):
    fields = ("hero_title", "hero_subtitle", "meta_title", "meta_description", "meta_keywords")


@register(Specialty)
class SpecialtyTR(TranslationOptions):
    fields = ("title", "description")


@register(Statistic)
class StatisticTR(TranslationOptions):
    fields = ("title",)


@register(WorkStep)
class WorkStepTR(TranslationOptions):
    fields = ("title", "description")


@register(ServiceCard)
class ServiceCardTR(TranslationOptions):
    fields = ("title", "description")


@register(Country)
class CountryTR(TranslationOptions):
    fields = ("name",)


@register(City)
class CityTR(TranslationOptions):
    fields = ("name",)
