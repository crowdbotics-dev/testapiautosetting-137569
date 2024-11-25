from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors137569ViewSet

router = DefaultRouter()
router.register(
    "testconnectors137569", Testconnectors137569ViewSet, basename="testconnectors137569"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
