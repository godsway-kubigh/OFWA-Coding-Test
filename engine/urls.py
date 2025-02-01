from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GalamsaySiteViewSet, GalamsayAnalysisViewSet

router = DefaultRouter()
router.register(r'sites', GalamsaySiteViewSet)
router.register(r'analysis', GalamsayAnalysisViewSet)

urlpatterns = [
    path('', include(router.urls)),
]