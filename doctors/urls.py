# doctors/urls.py
from django.urls import path
from .views import DoctorListView, DoctorDetailView

urlpatterns = [
    path("", DoctorListView.as_view(), name="doctors-list"),
    path("<slug:slug>/", DoctorDetailView.as_view(), name="doctors-detail"),
]
