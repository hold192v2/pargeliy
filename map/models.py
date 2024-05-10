from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Types(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(unique=True, max_length=200, blank=True, null=True, verbose_name="URL")
    class Meta:
        db_table = "type"
        verbose_name = "Тип"
        verbose_name_plural = "Типы"
    def __str__(self):
        return self.name
# Create your models here.
class Cardss(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(unique=True, max_length=200, blank=True, null=True, verbose_name='URL')
    image = models.ImageField(upload_to='map_images', blank=True, null=True, verbose_name='Изображение')
    rate = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(5)], blank= True, null=True, verbose_name='Оценка')
    author = models.CharField(max_length=150, blank=True, null=True, verbose_name='Автор')
    adress = models.CharField(max_length=150, blank=True, null=True, verbose_name='Адрес')
    info = models.TextField(blank=True, null=True, verbose_name='Информация об Объекте')
    type = models.ForeignKey(to=Types, on_delete=models.PROTECT, verbose_name='Тип')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "cardss"
        verbose_name = "Карточка"
        verbose_name_plural = "Карточки"
