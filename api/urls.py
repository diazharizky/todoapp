from django.urls import path, include
from .v1 import urls as v1_path
from .v2 import urls as v2_path

urlpatterns = [
    path("v1/", include(v1_path)),
    path("v2/", include(v2_path)),
]
