from rest_framework import generics
from sensors.models import SensorsData
from .serializers import SensorsDataListSerializer, SensorsDataCreateSerializer


class SensorsDataListAPIView(generics.ListAPIView):
    queryset = SensorsData.objects.all()
    serializer_class = SensorsDataListSerializer


class SensorsDataCreateAPIView(generics.CreateAPIView):
    queryset = SensorsData.objects.all()
    serializer_class = SensorsDataCreateSerializer
