from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import ConsultationRequest
from .serializers import ConsultationRequestSerializer


class ConsultationRequestListCreateView(generics.ListCreateAPIView):
    """
    Barcha so‘rovlarni olish yoki yangi so‘rov yuborish
    """
    queryset = ConsultationRequest.objects.all()
    serializer_class = ConsultationRequestSerializer

    @swagger_auto_schema(
        operation_summary="So‘rovlar ro‘yxati va yangi so‘rov yuborish",
        responses={200: ConsultationRequestSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Yangi so‘rov yuborish",
        responses={201: ConsultationRequestSerializer()},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
