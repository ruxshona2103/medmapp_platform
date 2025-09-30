# doctors/models.py
from django.db import models
from django.utils.text import slugify
from core.models import Specialty
from clinics.models import Hospital

class Doctor(models.Model):
    full_name = models.CharField("To‘liq ism", max_length=255)
    specialty_title = models.CharField("Mutaxassislik (matn)", max_length=255)
    photo = models.ImageField("Rasm", upload_to="doctors/", blank=True, null=True)
    slug = models.SlugField("Slug", unique=True, max_length=255)

    hospitals = models.ManyToManyField(Hospital, verbose_name="Klinikalar", related_name="doctors", blank=True)
    rating = models.FloatField("Reyting", default=0)
    experience_years = models.PositiveIntegerField("Tajriba (yil)", default=0)
    surgeries_count = models.PositiveIntegerField("Amaliyotlar soni", default=0)
    is_popular = models.BooleanField("Ommabop", default=False)
    resume_file = models.FileField("Rezyume", upload_to="doctors/resumes/", blank=True, null=True)

    # SEO
    meta_title = models.CharField("Meta sarlavha", max_length=255, blank=True)
    meta_description = models.TextField("Meta tavsif", blank=True)
    meta_keywords = models.CharField("Meta kalit so‘zlar", max_length=500, blank=True)

    # ixtiyoriy: bog‘lash uchun haqiqiy Specialty modeli (frontendga kerak bo‘lsa)
    specialty = models.ForeignKey(Specialty, verbose_name="Mutaxassislik (model)", on_delete=models.SET_NULL, null=True, blank=True, related_name="doctors")

    published_at = models.DateTimeField("Qo‘shilgan vaqt", auto_now_add=True)

    class Meta:
        verbose_name = "Shifokor"
        verbose_name_plural = "Shifokorlar"
        ordering = ["-is_popular", "full_name"]

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.full_name)
        super().save(*args, **kwargs)
