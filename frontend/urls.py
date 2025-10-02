from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),                        # / → index.html
    path("clinics/", views.clinics, name="clinics"),          # /clinics/ → clinics.html
    path("blog/", views.blog, name="blog"),                   # /blog/ → blog.html
    path("doctors/", views.doctors, name="doctors"),          # /doctors/ → doctors.html
    path("services/", views.services, name="services"),       # /services/ → services.html
]
