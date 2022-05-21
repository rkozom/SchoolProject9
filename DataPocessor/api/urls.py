from django.urls import path
from .views import SensorsDataListAPIView, SensorsDataCreateAPIView

urlpatterns = [
    path('getdata/', SensorsDataListAPIView.as_view()),
    path('postdata/', SensorsDataCreateAPIView.as_view()),
]