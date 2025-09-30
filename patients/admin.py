# patients/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import UserProfile, Testimonial

User = get_user_model()

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = True
    extra = 0

class UserAdmin(BaseUserAdmin):
    inlines = [UserProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Testimonial)
class TestimonialAdmin(TabbedTranslationAdmin, admin.ModelAdmin):
    list_display = ("patient_name", "country", "treatment_received", "is_featured", "created_at")
    list_filter = ("is_featured", "country")
    search_fields = ("patient_name", "treatment_received", "review_text")
