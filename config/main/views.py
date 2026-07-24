from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Contract
from .serializers import ContractSerializer

@method_decorator(csrf_exempt, name='dispatch')
class ContractViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [AllowAny]
    authentication_classes = []
