"""File containing URLs"""

from django.urls import path, include
from api import urls as api_path

urlpatterns = [
    path("api/", include(api_path)),
]
