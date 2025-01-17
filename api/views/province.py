from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from ..serializers import *
from ..models import *

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, extend_schema_view
from drf_spectacular.types import OpenApiTypes


# 2) PROVINCE   
class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all().order_by('province_id')
    serializer_class = ProvinceSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]

