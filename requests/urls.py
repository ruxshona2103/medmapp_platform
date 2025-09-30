from django.urls import path
from .views import ConsultationRequestListCreateView

urlpatterns = [
    path("consultations/", ConsultationRequestListCreateView.as_view(), name="consultations"),
]
