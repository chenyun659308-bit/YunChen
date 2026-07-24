from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContractViewSet

router = DefaultRouter()
router.register(r'contact', ContractViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls)),
]
