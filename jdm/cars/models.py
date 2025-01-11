from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)
    available = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')
    marka_car = models.CharField(max_length=100, blank=True, null=True)  # Марка автомобиля
    color_car = models.CharField(max_length=100, blank=True, null=True)  # Цвет автомобиля
    country_car = models.CharField(max_length=100, blank=True, null=True)  # Страна производства
    year_car = models.PositiveIntegerField(blank=True, null=True)  # Год изготовления
    mileage_car = models.PositiveIntegerField(blank=True, null=True)  # Пробег
    engine_car = models.CharField(max_length=100, blank=True, null=True)  # Тип двигателя
    transmission_car = models.CharField(max_length=50, blank=True, null=True)  # Трансмиссия
    hand_drive = models.CharField(max_length=50, blank=True, null=True)  # Левый/правый руль
    type_oil = models.CharField(max_length=50, blank=True, null=True)  # Тип масла
    gear_car = models.CharField(max_length=50, blank=True, null=True)  # Привод

    def __str__(self):
        return self.name