from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType


def get_product_url(obj, view_name):
    ct_model = obj.__class__.meta.model_name
    return reverse(view_name, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    country = models.CharField(max_length=255, verbose_name='Страна производитель')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title


class Kitchen(Product):
    size = models.CharField(max_length=255, verbose_name='Размер (ШxВxГ)')
    material = models.CharField(max_length=255, verbose_name='Материал')
    color = models.CharField(max_length=255, verbose_name='Цвет')

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def __str__(self):
        return '{} : {}'.format(self.category.name, self.title)


class Sofa(Product):
    size = models.CharField(max_length=255, verbose_name='Размер (ШxВxГ)')
    material = models.CharField(max_length=255, verbose_name='Материал')
    color = models.CharField(max_length=255, verbose_name='Цвет')
    filler = models.CharField(max_length=255, verbose_name='Наполнитель')

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def __str__(self):
        return '{} : {}'.format(self.category.name, self.title)


class Lamp(Product):
    power = models.CharField(max_length=255, verbose_name='Мощность')
    brightness = models.CharField(max_length=255, verbose_name='Яркость')
    rgb = models.BooleanField(default=True)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    def __str__(self):
        return '{} : {}'.format(self.category.name, self.title)
