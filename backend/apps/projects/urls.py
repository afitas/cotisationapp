from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjetViewSet, ProjetBlocViewSet, CotisationProjetViewSet

router = DefaultRouter()
router.register(r'projets', ProjetViewSet)
router.register(r'blocs', ProjetBlocViewSet)
router.register(r'cotisations-projet', CotisationProjetViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 