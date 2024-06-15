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

class Areas(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название района")
    slug = models.SlugField(unique=True, max_length=200, blank=True, null=True, verbose_name="URL")
    class Meta:
        db_table = "area"
        verbose_name = "Район"
        verbose_name_plural = "Районы"
    def __str__(self):
        return self.name

class Cardss(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(unique=True, max_length=200, blank=True, null=True, verbose_name='URL')
    image = models.ImageField(upload_to='static/deps/media', blank=True, null=True, verbose_name='Изображение')
    rate = models.DecimalField(default=0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], max_digits=2, decimal_places=1, blank= True, null=True, verbose_name='Оценка')
    author = models.CharField(max_length=150, blank=True, null=True, verbose_name='Автор')
    adress = models.CharField(max_length=150, blank=True, null=True, verbose_name='Адрес')
    coordinates = models.CharField(max_length=15000, blank=True, null=True, verbose_name='Координаты 2GIS')
    info = models.TextField(blank=True, null=True, verbose_name='Информация об Объекте')
    area = models.ForeignKey(to=Areas, on_delete=models.PROTECT, verbose_name='Район', blank=True, null=True)
    type = models.ForeignKey(to=Types, on_delete=models.PROTECT, verbose_name='Тип')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/rating/%s" % self.slug
    class Meta:
        db_table = "cardss"
        verbose_name = "Карточка"
        verbose_name_plural = "Карточки"
