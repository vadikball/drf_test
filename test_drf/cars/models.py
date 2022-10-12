import uuid

from django.utils.timezone import now
from django.db import models
from datetime import date


class Color(models.Model):
    name = models.CharField('цвет', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "content\".\"color"
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class Brand(models.Model):
    name = models.CharField('марка', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "content\".\"brand"
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'


class CarModel(models.Model):
    name = models.CharField('модель', max_length=255)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return "{0} {1}".format(self.brand.name, self.name)

    class Meta:
        db_table = "content\".\"car_model"
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'


class Order(models.Model):
    color = models.ForeignKey('Color', on_delete=models.CASCADE, null=False)
    car_model = models.ForeignKey('CarModel', on_delete=models.CASCADE, null=False)
    amount = models.PositiveIntegerField('количество')
    date = models.DateField('дата заказа', default=now, blank=True)

    def __str__(self):
        return "{0} {1} Количество: {2} Дата: {3}".format(
            self.color,
            self.car_model,
            self.amount,
            self.date
        )

    class Meta:
        db_table = "content\".\"order"
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
