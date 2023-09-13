"""save it for later"""

from django.urls import path, include
from .v1 import urls as v1_path

urlpatterns = [
    path("v1/", include(v1_path)),
]
