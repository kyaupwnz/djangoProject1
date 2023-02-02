from django.db import models
from django.urls import reverse
from pytils.translit import slugify


# Create your models here.
NULLABALE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.id} {self.category_name}'


class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='Продукт')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='product/', verbose_name='Изображение', **NULLABALE)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    unit_price = models.IntegerField(verbose_name='Цена товара')
    date_of_creation = models.DateField(auto_now=True, verbose_name='Дата создания')
    date_of_last_changes = models.DateTimeField(verbose_name='Дата последнего изменения')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
       return f'{self.id} {self.product_name} {self.unit_price} {self.category.category_name}'


class Version(models.Model):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    STATUS = (
        ('active', 'активная'),
        ('inactive', 'неактивная')
    )

    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
    version_number = models.FloatField(default=1, verbose_name='Номер версии')
    version_name = models.CharField(max_length=50, verbose_name='Название версии')
    version_status = models.CharField(choices=STATUS, default=INACTIVE, verbose_name='текущая версия', max_length=10)


class Record(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    slug = models.SlugField(max_length=50, default='', null=False, verbose_name="URL")
    content = models.TextField(verbose_name='Содержимое', **NULLABALE)
    image = models.ImageField(upload_to='Wlog_image/', verbose_name='Изображение', **NULLABALE)
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_public = models.BooleanField(default=True, verbose_name='Опубликованно')
    views_counter = models.IntegerField(default=0, verbose_name='Счетчик просмотров')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

