from django.contrib import admin
from .models import Sensor, SensorsData


admin.site.site_header = "Администрирование системы сбора данных с датчиков"

admin.site.register(Sensor)
admin.site.register(SensorsData)
