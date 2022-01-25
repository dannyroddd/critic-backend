from django.urls import path

from .views import CriticViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', CriticViewSet, basename='critics')
urlpatterns = router.urls