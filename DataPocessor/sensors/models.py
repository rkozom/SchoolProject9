from tabnanny import verbose
from django.db import models


class Sensor(models.Model):
    """
    Датчик
    """
    name = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание', max_length=250)

    class Meta:
        verbose_name = "Датчик"
        verbose_name_plural = "Датчики"
        ordering = ('name',)

    def __str__(self):
        return self.name


class SensorsData(models.Model):
    """
    Данные, полученные с датчиков
    """
    measurement_time = models.DateTimeField(verbose_name='Время измерения', auto_now_add=True)
    temperature = models.DecimalField(verbose_name='Температура', max_digits=5, decimal_places=2)
    humidity = models.DecimalField(verbose_name='Влажность', max_digits=5, decimal_places=2)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, verbose_name='Сенсор')

    class Meta:
        verbose_name = "Данные с датчиков"
        ordering = ('measurement_time',)
    
    def __str__(self):
        return f'Измерение с датчика {self.sensor} в {self.measurement_time}: T = {self.temperature}, H = {self.humidity}'

