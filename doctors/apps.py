# doctors/apps.py
from django.apps import AppConfig

class DoctorsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "doctors"

    def ready(self):
        import doctors.translation  # noqa
