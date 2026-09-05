from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Contract, Product
from .serializers import ContractSerializer, ProductSerializer

@method_decorator(csrf_exempt, name='dispatch')
class ContractViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [AllowAny]
    authentication_classes = []


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(active=True)
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    authentication_classes = []
