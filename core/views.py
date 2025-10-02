from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import SiteSettings, Specialty, Statistic, WorkStep, ServiceCard
from .serializers import (
    SiteSettingsSerializer, SpecialtySerializer,
    StatisticSerializer, WorkStepSerializer, ServiceCardSerializer
)


class HomePageView(APIView):
    """
    Bosh sahifa ma'lumotlari
    """
    @swagger_auto_schema(
        operation_id="v1_home_list",
        operation_summary="Bosh sahifa ma'lumotlari",
        operation_description="Hero, sozlamalar, specialties, statistikalar, ish bosqichlari va xizmatlar bloklarini qaytaradi.",
        responses={
            200: openapi.Response(
                "Bosh sahifa JSON",
                schema=openapi.Schema(type=openapi.TYPE_OBJECT)
            )
        }
    )
    def get(self, request):
        settings = SiteSettings.get_solo()
        data = {
            "settings": SiteSettingsSerializer(settings).data,
            "specialties": SpecialtySerializer(Specialty.objects.all(), many=True).data,
            "statistics": StatisticSerializer(Statistic.objects.all(), many=True).data,
            "steps": WorkStepSerializer(WorkStep.objects.all(), many=True).data,
            "services": ServiceCardSerializer(ServiceCard.objects.all(), many=True).data,
        }
        return Response(data)

