# doctors/admin.py
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(TabbedTranslationAdmin, admin.ModelAdmin):
    list_display = ("full_name", "specialty_title", "is_popular", "rating", "experience_years")
    list_filter = ("is_popular", "hospitals", "specialty")
    search_fields = ("full_name", "specialty_title")
    filter_horizontal = ("hospitals",)
    prepopulated_fields = {"slug": ("full_name",)}
    fieldsets = (
        ("Asosiy", {"fields": ("full_name", "specialty", "specialty_title", "photo", "slug")}),
        ("Ko‘rsatkichlar", {"fields": ("rating", "experience_years", "surgeries_count", "is_popular")}),
        ("Fayl", {"fields": ("resume_file",)}),
        ("SEO", {"fields": ("meta_title", "meta_description", "meta_keywords")}),
    )
