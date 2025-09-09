from rest_framework import viewsets, mixins
from drf_yasg.utils import swagger_auto_schema
from .models import Country, City, CounterStat, HowItWorksStep, ServiceCard
from .serializers import CountrySer, CitySer, CounterStatSer, HowItWorksStepSer, ServiceCardSer


class ReadOnlyVS(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """Faqat o'qish (list/retrieve) uchun umumiy ViewSet."""
    pass

CORE_TAG = ["core"]


class CountryViewSet(ReadOnlyVS):
    queryset = Country.objects.all().order_by("order_index", "translations__name")
    serializer_class = CountrySer

    @swagger_auto_schema(operation_summary="Davlatlar ro'yxati", tags=CORE_TAG)
    def list(self, request, *args, **kwargs): return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Davlat tafsiloti", tags=CORE_TAG)
    def retrieve(self, request, *args, **kwargs): return super().retrieve(request, *args, **kwargs)


class CityViewSet(ReadOnlyVS):
    queryset = City.objects.select_related("country").all()
    serializer_class = CitySer

    @swagger_auto_schema(operation_summary="Shaharlar ro'yxati", tags=CORE_TAG)
    def list(self, request, *args, **kwargs): return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Shahar tafsiloti", tags=CORE_TAG)
    def retrieve(self, request, *args, **kwargs): return super().retrieve(request, *args, **kwargs)


class CounterStatViewSet(ReadOnlyVS):
    queryset = CounterStat.objects.filter(is_active=True).order_by("order_index")
    serializer_class = CounterStatSer

    @swagger_auto_schema(operation_summary="Statistikalar", tags=CORE_TAG)
    def list(self, request, *args, **kwargs): return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Statistika tafsiloti", tags=CORE_TAG)
    def retrieve(self, request, *args, **kwargs): return super().retrieve(request, *args, **kwargs)


class HowItWorksStepViewSet(ReadOnlyVS):
    queryset = HowItWorksStep.objects.filter(is_active=True).order_by("order_index")
    serializer_class = HowItWorksStepSer

    @swagger_auto_schema(operation_summary="'Biz qanday ishlaymiz?' qadamlar", tags=CORE_TAG)
    def list(self, request, *args, **kwargs): return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Qadam tafsiloti", tags=CORE_TAG)
    def retrieve(self, request, *args, **kwargs): return super().retrieve(request, *args, **kwargs)


class ServiceCardViewSet(ReadOnlyVS):
    queryset = ServiceCard.objects.filter(is_active=True).order_by("order_index")
    serializer_class = ServiceCardSer

    @swagger_auto_schema(operation_summary="Xizmatlar ro'yxati", tags=CORE_TAG)
    def list(self, request, *args, **kwargs): return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Xizmat tafsiloti", tags=CORE_TAG)
    def retrieve(self, request, *args, **kwargs): return super().retrieve(request, *args, **kwargs)
