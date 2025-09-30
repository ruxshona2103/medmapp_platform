from modeltranslation.translator import register, TranslationOptions
from .models import ServiceIntro, JourneyStep, JourneyStepItem

@register(ServiceIntro)
class ServiceIntroTR(TranslationOptions):
    fields = ("title", "subtitle", "button_text", "meta_title", "meta_description", "meta_keywords")

@register(JourneyStep)
class JourneyStepTR(TranslationOptions):
    fields = ("title", "description")

@register(JourneyStepItem)
class JourneyStepItemTR(TranslationOptions):
    fields = ("text",)
