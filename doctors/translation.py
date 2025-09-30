# doctors/translation.py
from modeltranslation.translator import register, TranslationOptions
from .models import Doctor

@register(Doctor)
class DoctorTR(TranslationOptions):
    fields = ("full_name", "specialty_title", "meta_title", "meta_description", "meta_keywords")
