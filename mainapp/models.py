from django.db import models


# Create your models here.

class CategoryProduct(models.Model):
    name = models.CharField(verbose_name='наименование категории', max_length=128, unique=True)
    description = models.TextField(verbose_name='описание категории', blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'


class Product(models.Model):
    category = models.ForeignKey(verbose_name='категория товара', to=CategoryProduct, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='наименование', max_length=128)
    image = models.ImageField(upload_to='prodacts_photo', blank=True, default='prodacts_photo/logo.png')
    short_descr = models.CharField(verbose_name='краткое описание товара', max_length=64, blank=True)
    description = models.TextField(verbose_name='описание товара', blank=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=12, decimal_places=2, default=0)
    quantity = models.IntegerField(verbose_name='количество на складе', default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} ({self.category.name})'
