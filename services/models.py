from django.db import models


class ServiceIntro(models.Model):
    # Xizmat sahifasi hero qismi
    title = models.CharField("Sarlavha", max_length=255)
    subtitle = models.TextField("Qisqa matn", blank=True)
    button_text = models.CharField("Tugma matni", max_length=120, default="Xizmatlar bilan tanishish")

    # SEO
    meta_title = models.CharField("Meta sarlavha", max_length=255, blank=True)
    meta_description = models.TextField("Meta tavsif", blank=True)
    meta_keywords = models.CharField("Meta kalit so‘zlar", max_length=500, blank=True)

    class Meta:
        verbose_name = "Xizmat intro"
        verbose_name_plural = "Xizmat introlar"

    def __str__(self):
        return self.title


class JourneyStep(models.Model):
    # “Sog‘ayish sari yo‘lingiz” timeline
    order = models.PositiveIntegerField("Tartib", default=0)  # drag&drop uchun
    step_number = models.PositiveIntegerField("Bosqich raqami")  # 1,2,3...
    title = models.CharField("Sarlavha", max_length=255)
    description = models.TextField("Tavsif")
    icon_svg = models.TextField("SVG ikona kodi", blank=True, help_text="SVG ikona kodi")

    class Meta:
        verbose_name = "Yo‘l bosqichi"
        verbose_name_plural = "Yo‘l bosqichlari"
        ordering = ["order", "step_number"]

    def __str__(self):
        return f"{self.step_number}. {self.title}"


class JourneyStepItem(models.Model):
    # Har bir bosqich ichidagi bandlar
    step = models.ForeignKey(
        JourneyStep,
        related_name="items",
        on_delete=models.CASCADE,
        verbose_name="Bosqich"
    )
    order = models.PositiveIntegerField("Tartib", default=0)
    text = models.CharField("Matn", max_length=500)

    class Meta:
        verbose_name = "Bosqich elementi"
        verbose_name_plural = "Bosqich elementlari"
        ordering = ["order"]

    def __str__(self):
        return self.text
