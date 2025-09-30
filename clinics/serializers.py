from rest_framework import serializers
from core.models import Country, City, Specialty
from .models import Hospital, HospitalGalleryImage, HospitalTreatmentPrice


class SpecialtyBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ("id", "title")


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "name")


class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = City
        fields = ("id", "name", "country")


class HospitalGalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalGalleryImage
        fields = ("id", "image")


class HospitalPriceSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = HospitalTreatmentPrice
        fields = ("id", "category", "procedure_name", "price")


class HospitalListSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    specialties = SpecialtyBriefSerializer(many=True, read_only=True)

    class Meta:
        model = Hospital
        fields = ("id", "name", "slug", "image", "city", "specialties", "is_popular")


class HospitalDetailSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    specialties = SpecialtyBriefSerializer(many=True, read_only=True)
    gallery = HospitalGalleryImageSerializer(many=True, read_only=True)
    prices = HospitalPriceSerializer(many=True, read_only=True)

    class Meta:
        model = Hospital
        fields = (
            "id", "name", "slug", "image", "hero_image",
            "description", "founded_year", "bed_count",
            "icu_bed_count", "operating_rooms_count",
            "city", "specialties", "is_popular",
            "infrastructure_details", "guest_house_details",
            "meta_title", "meta_description", "meta_keywords",
            "gallery", "prices",
        )
