from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.db.models import Q

from .models import Doctor
from .serializers import DoctorListSerializer, DoctorDetailSerializer


class DoctorListView(generics.ListAPIView):
    """
    Shifokorlar ro‘yxati
    """
    serializer_class = DoctorListSerializer

    @swagger_auto_schema(
        operation_id="v1_doctors_list",
        operation_summary="Shifokorlar ro‘yxati (filtrlar bilan)",
        manual_parameters=[
            openapi.Parameter("specialty", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description="Specialty ID"),
            openapi.Parameter("country", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description="Country ID (shifokor ishlayotgan klinikalar orqali)"),
            openapi.Parameter("city", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description="City ID"),
            openapi.Parameter("search", openapi.IN_QUERY, type=openapi.TYPE_STRING, description="Ism yoki mutaxassislik bo‘yicha qidiruv"),
            openapi.Parameter("popular", openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN, description="Faqat ommabop shifokorlar"),
        ]
    )
    def get_queryset(self):
        qs = Doctor.objects.prefetch_related("hospitals", "hospitals__city", "hospitals__city__country", "hospitals__specialties")

        s = self.request.GET.get("specialty")
        c = self.request.GET.get("country")
        city = self.request.GET.get("city")
        q = self.request.GET.get("search")
        popular = self.request.GET.get("popular")

        if s:
            qs = qs.filter(hospitals__specialties__id=s)  # Specialty orqali filter
        if c:
            qs = qs.filter(hospitals__city__country_id=c)
        if city:
            qs = qs.filter(hospitals__city_id=city)
        if q:
            qs = qs.filter(Q(full_name__icontains=q) | Q(specialty_title__icontains=q))
        if popular in ("1", "true", "True"):
            qs = qs.filter(is_popular=True)

        return qs.distinct().order_by("-is_popular", "full_name")


class DoctorDetailView(generics.RetrieveAPIView):
    """
    Shifokor ma’lumotlari (slug bo‘yicha)
    """
    lookup_field = "slug"
    queryset = Doctor.objects.prefetch_related("hospitals", "hospitals__city", "hospitals__city__country")
    serializer_class = DoctorDetailSerializer

    @swagger_auto_schema(
        operation_id="v1_doctors_read",
        operation_summary="Shifokor ma’lumotlari (slug bo‘yicha)",

    )
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)
