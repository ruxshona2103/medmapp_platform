from modeltranslation.translator import register, TranslationOptions
from .models import Hospital, PriceCategory, HospitalTreatmentPrice

@register(Hospital)
class HospitalTR(TranslationOptions):
    fields = ("name", "description", "infrastructure_details", "guest_house_details",
              "meta_title", "meta_description", "meta_keywords")

@register(PriceCategory)
class PriceCategoryTR(TranslationOptions):
    fields = ("name",)

@register(HospitalTreatmentPrice)
class HospitalTreatmentPriceTR(TranslationOptions):
    fields = ("procedure_name",)
