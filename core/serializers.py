from rest_framework import serializers
from django.utils.translation import get_language
from .models import Country, City, CounterStat, HowItWorksStep, ServiceCard


def lang_value(obj, field):
    """Aktiv til bo'yicha tarjima qiymatini qaytaradi; bo'lmasa fallback."""
    lang = get_language() or "uz"
    return obj.safe_translation_getter(field, language_code=lang, any_language=True)


def all_translations(obj, fields):
    """Barcha tarjimalarni qaytaradi (uz/ru/en)."""
    out = []
    for tr in obj.translations.all():
        item = {"language_code": tr.language_code}
        for f in fields:
            item[f] = getattr(tr, f, None)
        out.append(item)
    return out


class CountrySer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    slug = serializers.SerializerMethodField()
    translations = serializers.SerializerMethodField()

    class Meta:
        model = Country
        fields = ("id", "iso2", "order_index", "name", "slug", "translations")

    def get_name(self, obj): return lang_value(obj, "name")
    def get_slug(self, obj): return lang_value(obj, "slug")
    def get_translations(self, obj): return all_translations(obj, ["name", "slug"])


class CitySer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    slug = serializers.SerializerMethodField()
    country = CountrySer(read_only=True)
    translations = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = ("id", "order_index", "name", "slug", "country", "translations")

    def get_name(self, obj): return lang_value(obj, "name")
    def get_slug(self, obj): return lang_value(obj, "slug")
    def get_translations(self, obj): return all_translations(obj, ["name", "slug"])


class CounterStatSer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()
    translations = serializers.SerializerMethodField()

    class Meta:
        model = CounterStat
        fields = ("label", "value_int", "icon", "translations")

    def get_label(self, obj): return lang_value(obj, "label")
    def get_translations(self, obj): return all_translations(obj, ["label"])


class HowItWorksStepSer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    translations = serializers.SerializerMethodField()

    class Meta:
        model = HowItWorksStep
        fields = ("order_index", "title", "description", "media", "translations")

    def get_title(self, obj): return lang_value(obj, "title")
    def get_description(self, obj): return lang_value(obj, "description")
    def get_translations(self, obj): return all_translations(obj, ["title", "description"])


class ServiceCardSer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    translations = serializers.SerializerMethodField()

    class Meta:
        model = ServiceCard
        fields = ("title", "description", "icon", "translations")

    def get_title(self, obj): return lang_value(obj, "title")
    def get_description(self, obj): return lang_value(obj, "description")
    def get_translations(self, obj): return all_translations(obj, ["title", "description"])
