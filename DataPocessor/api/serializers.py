from dataclasses import fields
from rest_framework import serializers
from sensors.models import SensorsData


class SensorsDataListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorsData
        fields = ('measurement_time', 'temperature', 'humidity', 'sensor')


class SensorsDataCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorsData
        fields = ('temperature', 'humidity', 'sensor')
