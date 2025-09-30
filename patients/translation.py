# patients/translation.py
from modeltranslation.translator import register, TranslationOptions
from .models import Testimonial, UserProfile

@register(Testimonial)
class TestimonialTR(TranslationOptions):
    fields = ("patient_name", "treatment_received", "review_text")

# UserProfiledagi faqat 'bio' tarjima qilamiz (kerak bo‘lsa)
@register(UserProfile)
class UserProfileTR(TranslationOptions):
    fields = ("bio",)
