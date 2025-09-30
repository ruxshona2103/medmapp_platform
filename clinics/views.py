from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from core.models import Country, City, Specialty
from .models import Hospital
from .serializers import (
    HospitalListSerializer, HospitalDetailSerializer,
    CountrySerializer, CitySerializer, SpecialtyBriefSerializer
)


class ClinicsFiltersView(APIView):
    """
    Klinikalar sahifasi uchun filterlar:
    - specialties
    - countries
    - cities (agar country_id berilsa, shu davlat shaharlari)
    """
    @swagger_auto_schema(
        operation_id="v1_clinics_filters_list",
        operation_summary="Klinikalar — filterlar",
        manual_parameters=[
            openapi.Parameter("country_id", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description="Country ID"),
        ],
        responses={200: "specialties, countries, cities"}
    )
    def get(self, request):
        country_id = request.GET.get("country_id")

        specialties = Specialty.objects.all().order_by("order")
        countries = Country.objects.all().order_by("name")

        if country_id:
            cities = City.objects.filter(country_id=country_id).order_by("name")
        else:
            cities = City.objects.all().order_by("name")

        return Response({
            "specialties": SpecialtyBriefSerializer(specialties, many=True).data,
            "countries": CountrySerializer(countries, many=True).data,
            "cities": CitySerializer(cities, many=True).data,
        })


class HospitalListView(generics.ListAPIView):
    """
    Klinikalar ro‘yxati (filtrlar: specialty, country, city, search)
    """
    serializer_class = HospitalListSerializer

    @swagger_auto_schema(
        operation_id="v1_clinics_list",   # Swagger uchun unique ID
        operation_summary="Klinikalar ro‘yxati",
        manual_parameters=[
            openapi.Parameter(
                "specialty", openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Specialty ID"
            ),
            openapi.Parameter(
                "country", openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Country ID"
            ),
            openapi.Parameter(
                "city", openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="City ID"
            ),
            openapi.Parameter(
                "search", openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Name bo‘yicha qidiruv"
            ),
        ]
    )
    def get(self, request, *args, **kwargs):
        """
        GET so‘rovi orqali barcha klinikalar ro‘yxatini qaytaradi
        (filtrlash parametrlari optional).
        """
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        qs = Hospital.objects.select_related("city", "city__country").prefetch_related("specialties")

        specialty = self.request.GET.get("specialty")
        country = self.request.GET.get("country")
        city = self.request.GET.get("city")
        search = self.request.GET.get("search")

        if specialty:
            qs = qs.filter(specialties__id=specialty)
        if country:
            qs = qs.filter(city__country_id=country)
        if city:
            qs = qs.filter(city_id=city)
        if search:
            qs = qs.filter(Q(name__icontains=search))

        return qs.distinct().order_by("name")



class HospitalDetailView(generics.RetrieveAPIView):
    """
    Klinikani batafsil ko‘rish (slug bo‘yicha)
    """
    lookup_field = "slug"
    queryset = Hospital.objects.select_related("city", "city__country").prefetch_related(
        "specialties", "gallery", "prices__category"
    )
    serializer_class = HospitalDetailSerializer

    @swagger_auto_schema(
        operation_id="v1_clinics_read",
        operation_summary="Klinika tafsilotlari (slug bo‘yicha)"
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
