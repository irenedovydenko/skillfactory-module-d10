from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Car(models.Model):
    T_CHOICES = (
        (1, 'Механика'),
        (2, 'Автомат'),
        (3, 'Робот'),
    )
    C_CHOICES = (
        (1, 'Чёрный'),
        (2, 'Белый'),
        (3, 'Красный'),
        (4, 'Оранжевый'),
        (5, 'Жёлтый'),
        (6, 'Зелёный'),
        (7, 'Голубой'),
        (8, 'Синий'),
        (9, 'Фиолетовый'),
    )

    vendor = models.CharField(max_length=50,
                              verbose_name='Производитель')
    model = models.CharField(max_length=50,
                             verbose_name='Модель авто')
    year = models.IntegerField(validators=[MinValueValidator(1900),
                                           MaxValueValidator(2020)],
                               verbose_name='Год выпуска')
    transmission = models.SmallIntegerField(choices=T_CHOICES,
                                            default=1,
                                            verbose_name='Коробка передач')
    color = models.SmallIntegerField(choices=C_CHOICES,
                                     verbose_name='Цвет',
                                     default=1)

    def __str__(self):
        return f'Автомобиль {self.model} марки {self.vendor}'

    class Meta:
        ordering = ('vendor', 'model',)