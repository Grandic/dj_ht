from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='продукт')
    description = models.TextField(max_length=300, verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='продукт')
    description = models.TextField(max_length=300, verbose_name='описание')
    image = models.ImageField(upload_to='categories/', verbose_name='изображение (превью)', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='цена за покупку')
    date_init = models.DateTimeField(max_length=50, verbose_name='дата создания')
    change_date = models.DateTimeField(max_length=50, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name} {self.price} {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)
