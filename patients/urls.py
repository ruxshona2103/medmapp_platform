# patients/urls.py
from django.urls import path
from .views import TestimonialListView, TestimonialDetailView

urlpatterns = [
    path("testimonials/", TestimonialListView.as_view(), name="testimonials-list"),
    path("testimonials/<int:id>/", TestimonialDetailView.as_view(), name="testimonials-detail"),
]
