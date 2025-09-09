from django.db import models
from django.utils.text import slugify
from django.utils import translation
from parler.models import TranslatableModel, TranslatedFields


class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Orderable(models.Model):
    order_index = models.PositiveIntegerField(default=0)
    class Meta:
        abstract = True
        ordering = ["order_index", "id"]


class Country(TranslatableModel, TimeStamped, Orderable):
    translations = TranslatedFields(
        name=models.CharField(max_length=120),
        slug=models.SlugField(max_length=140, blank=True),
    )
    iso2 = models.CharField(max_length=2, blank=True, default="")

    def save(self, *args, **kwargs):
        # Faol tilni aniqlaymiz (yo‘q bo‘lsa 'uz')
        lang = translation.get_language() or "uz"
        self.set_current_language(lang)
        tr = self.get_translation(lang, auto_create=True)  # <-- to'g'ri metod
        if not tr.slug and tr.name:
            tr.slug = slugify(tr.name)
        self.iso2 = (self.iso2 or "").upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.safe_translation_getter("name", any_language=True) or f"Country {self.pk}"


class City(TranslatableModel, TimeStamped, Orderable):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="cities")
    translations = TranslatedFields(
        name=models.CharField(max_length=120),
        slug=models.SlugField(max_length=140, blank=True),
    )

    def save(self, *args, **kwargs):
        lang = translation.get_language() or "uz"
        self.set_current_language(lang)
        tr = self.get_translation(lang, auto_create=True)  # <-- to'g'ri metod
        if not tr.slug and tr.name:
            tr.slug = slugify(tr.name)
        super().save(*args, **kwargs)

    def __str__(self):
        nm = self.safe_translation_getter("name", any_language=True) or f"City {self.pk}"
        return f"{nm}, {self.country.iso2 or '??'}"


class CounterStat(TranslatableModel, Orderable, TimeStamped):
    translations = TranslatedFields(label=models.CharField(max_length=160))
    value_int = models.PositiveIntegerField(default=0)
    icon = models.CharField(max_length=120, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.safe_translation_getter('label', any_language=True)} = {self.value_int}"


class HowItWorksStep(TranslatableModel, Orderable, TimeStamped):
    translations = TranslatedFields(
        title=models.CharField(max_length=160),
        description=models.TextField(blank=True),
    )
    media = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.order_index}. {self.safe_translation_getter('title', any_language=True)}"


class ServiceCard(TranslatableModel, Orderable, TimeStamped):
    translations = TranslatedFields(
        title=models.CharField(max_length=160),
        description=models.TextField(blank=True),
    )
    icon = models.CharField(max_length=120, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or f"Service {self.pk}"
