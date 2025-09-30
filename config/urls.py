from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="MedMapp API",
        default_version="v1",
        description="MedMapp uchun REST API hujjatlari",
        contact=openapi.Contact(email="info@medmapp.uz"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/core", include("core.urls")),
    path("api/v1/services", include("services.urls")),
    path("api/v1/clinics", include("clinics.urls")),
    path("api/v1/doctors/", include("doctors.urls")),
    path("api/v1/blog/", include("blog.urls")),
    path("api/v1/patients/", include("patients.urls")),
    path("api/v1/requests/", include("requests.urls")),



    # Swagger / Redoc
    re_path(r"^swagger(?P<format>\.json|\.yaml)$",
            schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),

    # Asosiy URL Swaggerga yo‘naltiriladi
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-root"),
]
