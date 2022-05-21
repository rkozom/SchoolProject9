from django.urls import path
from .views import SensorDataListView

urlpatterns = [
    path('', SensorDataListView.as_view(), name='home')
]
