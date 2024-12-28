from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AnneeAbonnementViewSet,
    PlanMensuelViewSet,
    CotisationViewSet
)

app_name = 'subscriptions'

router = DefaultRouter()
router.register(r'annees', AnneeAbonnementViewSet)
router.register(r'plans', PlanMensuelViewSet)
router.register(r'cotisations', CotisationViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 