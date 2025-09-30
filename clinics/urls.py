# clinics/urls.py
from django.urls import path
from .views import ClinicsFiltersView, HospitalListView, HospitalDetailView

urlpatterns = [
    path("filters/", ClinicsFiltersView.as_view(), name="v1_clinics_filters_list"),
    path("", HospitalListView.as_view(), name="v1_clinics_list"),          # 👈 bu qo‘shilishi kerak
    path("<slug:slug>/", HospitalDetailView.as_view(), name="v1_clinics_read"),
]
