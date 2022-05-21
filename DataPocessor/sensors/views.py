from django.views.generic import ListView
from django.db.models import Avg
from .models import SensorsData
from typing import Any, Dict
import qsstats
import datetime


class SensorDataListView(ListView):
    model = SensorsData
    template_name = 'sensors_data_list.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        start = datetime.datetime.now() - datetime.timedelta(seconds=30)
        qs = SensorsData.objects.select_related().filter(measurement_time__gt=start)
        context['chart_data'] = qs
        context['total_count'] = SensorsData.objects.count()
        return context
