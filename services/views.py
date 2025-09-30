from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import ServiceIntro, JourneyStep
from .serializers import ServiceIntroSerializer, JourneyStepSerializer, SpecialtyBriefSerializer
from core.models import Specialty

class ServicesPageView(APIView):
    """
    Xizmatlar sahifasi ma'lumotlari (hero, bosqichlar, mutaxassisliklar).
    """
    @swagger_auto_schema(
        operation_id="v1_services_list",
        operation_summary="Xizmatlar sahifasi",
        responses={200: "Intro, steps, specialties"},
    )
    def get(self, request):
        intro = ServiceIntro.objects.first()
        steps = JourneyStep.objects.prefetch_related("items").order_by("order", "step_number")
        specialties = Specialty.objects.order_by("order")
        return Response({
            "intro": ServiceIntroSerializer(intro).data if intro else None,
            "steps": JourneyStepSerializer(steps, many=True).data,
            "specialties": SpecialtyBriefSerializer(specialties, many=True).data,
        })
