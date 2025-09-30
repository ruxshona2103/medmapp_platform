from django.db import models


class ConsultationRequest(models.Model):
    STATUS_CHOICES = [
        ("new", "Yangi"),
        ("reviewed", "Ko‘rib chiqildi"),
    ]

    resident_of = models.CharField("Qayerdan", max_length=255)
    treatment = models.CharField("Davolanish turi", max_length=255)
    phone_number = models.CharField("Telefon raqami", max_length=20)
    created_at = models.DateTimeField("Yaratilgan vaqt", auto_now_add=True)
    status = models.CharField("Holati", max_length=20, choices=STATUS_CHOICES, default="new")

    class Meta:
        verbose_name = "So‘rov"
        verbose_name_plural = "So‘rovlar"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.resident_of} — {self.treatment}"
