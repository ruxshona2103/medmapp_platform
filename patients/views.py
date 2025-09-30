# patients/views.py
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.db.models import Q
from .models import Testimonial
from .serializers import TestimonialListSerializer, TestimonialDetailSerializer


class TestimonialListView(generics.ListAPIView):
    """
    Bemor sharhlari ro‘yxati
    """
    serializer_class = TestimonialListSerializer

    @swagger_auto_schema(
        operation_id="v1_testimonials_list",
        operation_summary="Sharhlar ro‘yxati (filtrlar bilan)",
        manual_parameters=[
            openapi.Parameter("featured", openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN, description="Faqat featured sharhlar"),
            openapi.Parameter("country", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description="Country ID"),
            openapi.Parameter("search", openapi.IN_QUERY, type=openapi.TYPE_STRING, description="Ism yoki davolanish bo‘yicha qidiruv"),
        ]
    )
    def get_queryset(self):
        qs = Testimonial.objects.select_related("country")

        featured = self.request.GET.get("featured")
        c = self.request.GET.get("country")
        q = self.request.GET.get("search")

        if featured in ("1", "true", "True"):
            qs = qs.filter(is_featured=True)
        if c:
            qs = qs.filter(country_id=c)
        if q:
            qs = qs.filter(
                Q(patient_name__icontains=q) |
                Q(treatment_received__icontains=q) |
                Q(review_text__icontains=q)
            )

        return qs.order_by("-is_featured", "-created_at")


class TestimonialDetailView(generics.RetrieveAPIView):
    """
    Sharhni batafsil ko‘rish (id bo‘yicha)
    """
    lookup_field = "id"
    queryset = Testimonial.objects.select_related("country")
    serializer_class = TestimonialDetailSerializer

    @swagger_auto_schema(
        operation_id="v1_testimonials_read",
        operation_summary="Sharhni batafsil ko‘rish"
    )
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)
