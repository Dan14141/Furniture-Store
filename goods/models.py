from django.db import models
from django.urls.base import reverse


class Category(models.Model):
    name = models.CharField(max_length=100,unique=True,verbose_name='Название')
    slug = models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ('id',)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100,unique=True,verbose_name='Название')
    slug = models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='URL')
    description = models.TextField(blank=True,null=True,verbose_name='Описание товара')
    image = models.ImageField(upload_to='goods_images',blank=True,null=True,verbose_name='Изображение')
    price = models.DecimalField(default=0.00,decimal_places=2,max_digits=10,verbose_name='Цена')
    discount = models.DecimalField(default=0.00,decimal_places=2,max_digits=4,verbose_name='Скидка')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name='Категория товара')

    def __str__(self):
        return f'{self.name}, количество - {self.quantity}'

    class Meta:
        db_table = 'Product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('id',)

    def display_id(self):
        return f'{self.id:05}'

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price

    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})

    def skidka_check(self):

        return f'{self.skidka_check}'