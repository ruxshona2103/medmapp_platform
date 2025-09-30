from django.db import models
from solo.models import SingletonModel


class SiteSettings(SingletonModel):
    """
    Saytning asosiy sozlamalari
    """

    hero_title = models.CharField("Bosh sarlavha", max_length=255)
    hero_subtitle = models.TextField("Qisqa matn", blank=True)
    hero_video = models.FileField("Reklama video", upload_to="hero/", blank=True, null=True)

    phone_number = models.CharField("Telefon raqam", max_length=64)
    email = models.EmailField("Email")
    address = models.CharField("Manzil", max_length=255)

    facebook_url = models.URLField("Facebook", blank=True)
    instagram_url = models.URLField("Instagram", blank=True)
    telegram_url = models.URLField("Telegram", blank=True)
    youtube_url = models.URLField("YouTube", blank=True)

    meta_title = models.CharField("Meta sarlavha", max_length=255, blank=True)
    meta_description = models.TextField("Meta tavsif", blank=True)
    meta_keywords = models.CharField("Meta kalit so‘zlar", max_length=500, blank=True)

    class Meta:
        verbose_name = "Sayt sozlamalari"
        verbose_name_plural = "Sayt sozlamalari"

    def __str__(self):
        return "Sayt sozlamalari"


class Specialty(models.Model):
    """Mutaxassisliklar (masalan: Kardiologiya, Ortopediya va h.k.)"""

    title = models.CharField("Nom", max_length=120)
    description = models.TextField("Tavsif", blank=True)
    icon_svg = models.TextField("SVG ikona", help_text="SVG kodini joylashtiring")
    order = models.PositiveIntegerField("Tartib", default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Mutaxassislik"
        verbose_name_plural = "Mutaxassisliklar"

    def __str__(self):
        return self.title


class Statistic(models.Model):
    """Statistik blok (masalan: 5000+ bemor, 20+ klinika)"""

    settings = models.ForeignKey(
        SiteSettings,
        on_delete=models.CASCADE,
        related_name="statistikalar",
        verbose_name="Sayt sozlamalari",
    )
    title = models.CharField("Nom", max_length=120)
    number = models.IntegerField("Son", default=0)
    icon_svg = models.TextField("SVG ikona", blank=True)
    order = models.PositiveIntegerField("Tartib", default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Statistika"
        verbose_name_plural = "Statistikalar"

    def __str__(self):
        return f"{self.title} ({self.number})"


class WorkStep(models.Model):
    """Biz qanday ishlaymiz? (bosqichlar)"""

    settings = models.ForeignKey(
        SiteSettings,
        on_delete=models.CASCADE,
        related_name="bosqichlar",
        verbose_name="Sayt sozlamalari",
    )
    step_number = models.PositiveIntegerField("Bosqich raqami")
    title = models.CharField("Sarlavha", max_length=160)
    description = models.TextField("Tavsif")

    class Meta:
        ordering = ["step_number"]
        verbose_name = "Ish bosqichi"
        verbose_name_plural = "Ish bosqichlari"

    def __str__(self):
        return f"{self.step_number}. {self.title}"


class ServiceCard(models.Model):
    """Xizmat kartalari"""

    settings = models.ForeignKey(
        SiteSettings,
        on_delete=models.CASCADE,
        related_name="xizmatlar",
        verbose_name="Sayt sozlamalari",
    )
    title = models.CharField("Sarlavha", max_length=160)
    description = models.TextField("Tavsif", blank=True)
    icon_svg = models.TextField("SVG ikona", help_text="SVG kodini joylashtiring")
    order = models.PositiveIntegerField("Tartib", default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Xizmat kartasi"
        verbose_name_plural = "Xizmat kartalari"

    def __str__(self):
        return self.title



class Country(models.Model):
    name = models.CharField("Davlat nomi", max_length=120, unique=True)

    class Meta:
        verbose_name = "Davlat"
        verbose_name_plural = "Davlatlar"
        ordering = ["name"]

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name="cities", verbose_name="Davlat")
    name = models.CharField("Shahar nomi", max_length=120)

    class Meta:
        verbose_name = "Shahar"
        verbose_name_plural = "Shaharlar"
        unique_together = ("country", "name")
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}, {self.country.name}"