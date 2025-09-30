from django.urls import path
from .views import ServicesPageView

urlpatterns = [
    path("v1/services/", ServicesPageView.as_view(), name="v1_services"),
]
