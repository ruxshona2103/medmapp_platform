# patients/serializers.py
from rest_framework import serializers
from core.models import Country
from .models import UserProfile, Testimonial

class CountryMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "name")

class UserProfileSerializer(serializers.ModelSerializer):
    country = CountryMiniSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = ("user", "photo", "bio", "country")

class TestimonialListSerializer(serializers.ModelSerializer):
    country = CountryMiniSerializer(read_only=True)
    class Meta:
        model = Testimonial
        fields = ("id", "patient_name", "country", "treatment_received", "photo", "video_url", "is_featured", "created_at")

class TestimonialDetailSerializer(serializers.ModelSerializer):
    country = CountryMiniSerializer(read_only=True)
    class Meta:
        model = Testimonial
        fields = ("id", "patient_name", "country", "treatment_received", "photo", "review_text", "video_url", "is_featured", "created_at")
