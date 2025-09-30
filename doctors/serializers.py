# doctors/serializers.py
from rest_framework import serializers
from core.models import Country, City
from clinics.models import Hospital
from .models import Doctor

class HospitalMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ("id", "name", "slug")

class DoctorListSerializer(serializers.ModelSerializer):
    hospitals = HospitalMiniSerializer(many=True, read_only=True)
    class Meta:
        model = Doctor
        fields = ("id", "full_name", "slug", "photo", "specialty_title", "is_popular", "rating", "hospitals")

class DoctorDetailSerializer(serializers.ModelSerializer):
    hospitals = HospitalMiniSerializer(many=True, read_only=True)
    class Meta:
        model = Doctor
        fields = (
            "id","full_name","slug","photo","specialty","specialty_title",
            "rating","experience_years","surgeries_count","is_popular",
            "resume_file","meta_title","meta_description","meta_keywords",
            "hospitals",
        )
