from django.db import models


# Create your models here

class GalaxyType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name='Тип галактики')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип галактики"
        verbose_name_plural = "Типы галактики"


class Galaxy(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Название')
    age = models.FloatField(default=0, verbose_name='Возраст')
    size = models.FloatField(default=0, verbose_name='Размер')
    type = models.ForeignKey('GalaxyType', verbose_name='Тип', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Галактика"
        verbose_name_plural = "Галактики"


class StarSystem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Название')
    age = models.FloatField(default=0, verbose_name='Возраст')
    radius = models.FloatField(default=0, verbose_name='Радиус')
    galaxy = models.ForeignKey('Galaxy', verbose_name='Галактика', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Звездная система"
        verbose_name_plural = "Звездные системы"


class Planet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Название')
    age = models.FloatField(default=0, verbose_name='Возраст')
    radius = models.FloatField(default=0, verbose_name='Радиус')
    mass = models.FloatField(default=0, verbose_name='Масса')
    habitable = models.BooleanField(default=False, choices=((False,'жизни нет'),(True,'возможна жизнь')), verbose_name='Обитаема ли')
    system = models.ForeignKey('StarSystem', verbose_name='Звездная система', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Планета"
        verbose_name_plural = "Планеты"


class Star(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Название')
    age = models.FloatField(default=0, verbose_name='Возраст')
    radius = models.FloatField(default=0, verbose_name='Радиус')
    mass = models.FloatField(default=0, verbose_name='Масса')
    temperature = models.FloatField(default=0, verbose_name='Температура')
    system = models.ForeignKey('StarSystem', verbose_name='Звездная система', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Звезда"
        verbose_name_plural = "Звезды"

