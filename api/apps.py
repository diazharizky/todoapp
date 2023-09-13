"""apps file"""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """config class"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "api"
