# patients/models.py
from django.db import models
from django.contrib.auth import get_user_model
from core.models import Country

User = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name="Foydalanuvchi", on_delete=models.CASCADE, related_name="profile")
    photo = models.ImageField("Rasm", upload_to="users/", blank=True, null=True)
    bio = models.TextField("Bio", blank=True)
    country = models.ForeignKey(Country, verbose_name="Mamlakat", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Foydalanuvchi profili"
        verbose_name_plural = "Foydalanuvchi profillari"

    def __str__(self):
        return f"Profil: {self.user}"

class Testimonial(models.Model):
    patient_name = models.CharField("Bemor ismi", max_length=255)
    country = models.ForeignKey(Country, verbose_name="Mamlakat", on_delete=models.SET_NULL, null=True, blank=True)
    photo = models.ImageField("Rasm", upload_to="testimonials/", blank=True, null=True)
    treatment_received = models.CharField("Olingan davolanish", max_length=255, blank=True)
    review_text = models.TextField("Sharh matni")
    video_url = models.URLField("Video URL", blank=True)
    is_featured = models.BooleanField("Tanlangan (featured)", default=False)
    created_at = models.DateTimeField("Yaratildi", auto_now_add=True)

    class Meta:
        verbose_name = "Sharh"
        verbose_name_plural = "Sharhlar"
        ordering = ["-is_featured", "-created_at"]

    def __str__(self):
        return f"{self.patient_name} — {self.treatment_received or ''}".strip()

