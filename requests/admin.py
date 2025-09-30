from django.contrib import admin
from .models import ConsultationRequest


@admin.register(ConsultationRequest)
class ConsultationRequestAdmin(admin.ModelAdmin):
    list_display = ("resident_of", "treatment", "phone_number", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("resident_of", "treatment", "phone_number")
    ordering = ("-created_at",)
