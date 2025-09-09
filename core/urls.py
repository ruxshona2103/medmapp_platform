from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, CityViewSet, CounterStatViewSet, HowItWorksStepViewSet, ServiceCardViewSet

app_name = "core"

router = DefaultRouter()
router.register(r"countries", CountryViewSet, basename="country")
router.register(r"cities", CityViewSet, basename="city")
router.register(r"counters", CounterStatViewSet, basename="counter")
router.register(r"how-it-works", HowItWorksStepViewSet, basename="how-it-works")
router.register(r"services", ServiceCardViewSet, basename="service")

urlpatterns = router.urls
