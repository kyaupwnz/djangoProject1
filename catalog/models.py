from django.db import models

# Create your models here.
NULLABALE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.id} {self.category_name}'

class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='Название продукта')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='product/', verbose_name='Изображение', **NULLABALE)
    # category = models.ForeignKey(Category, verbose_name='Название категории', on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50, verbose_name='Название категории')
    unit_price = models.IntegerField(verbose_name='Цена товара')
    date_of_creation = models.DateField(auto_now=True, verbose_name='Дата создания')
    date_of_last_changes = models.DateTimeField(verbose_name='Дата последнего изменения')


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


    def __str__(self):
        return f'{self.id} {self.product_name} {self.unit_price} {self.category_name}'




