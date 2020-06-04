# Generated by Django 3.0.6 on 2020-05-25 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carscat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.SmallIntegerField(choices=[(1, 'Чёрный'), (2, 'Белый'), (3, 'Красный'), (4, 'Оранжевый'), (5, 'Жёлтый'), (6, 'Зелёный'), (7, 'Голубой'), (8, 'Синий'), (9, 'Фиолетовый')], default=1, verbose_name='Цвет'),
        ),
    ]