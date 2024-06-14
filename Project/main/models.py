from django.db import models

class Articles(models.Model):
    image = models.CharField('Изображение', max_length=250)
    name= models.CharField('Название пиццы', max_length=20)
    price=models.CharField('price', max_length=5)
    description=models.TextField('Краткое описание')

    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
# Create your models here.

class Public(models.Model):
    login = models.CharField("Логин", max_length=20)
    comment = models.TextField("Логин")


    def __str__(self):
        return self.login
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class Drink(models.Model):
    image = models.CharField('Изображение', max_length=250)
    name= models.CharField('Название напитка', max_length=20)
    price=models.CharField('price', max_length=5)
    description=models.TextField('Краткое описание')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Напиток"
        verbose_name_plural = "Напитки"


class Combo(models.Model):
    image = models.CharField('Изображение', max_length=250)
    name= models.CharField('Название напитка', max_length=20)
    price=models.CharField('price', max_length=5)
    description=models.TextField('Краткое описание')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Комбо"
        verbose_name_plural = "Комбо"

class Role(models.Model):
    image = models.CharField('Изображение', max_length=250)
    name= models.CharField('Название напитка', max_length=20)
    price=models.CharField('price', max_length=5)
    description=models.TextField('Краткое описание')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Ролл"
        verbose_name_plural = "Роллы"

class Dessert(models.Model):
    image = models.CharField('Изображение', max_length=250)
    name= models.CharField('Название напитка', max_length=20)
    price=models.CharField('price', max_length=5)
    description=models.TextField('Краткое описание')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Десерт"
        verbose_name_plural = "Десерты"


class MainProduct(models.Model):
    image = models.CharField('Изображение', max_length=250)
    name= models.CharField('Название напитка', max_length=20)
    price=models.CharField('price', max_length=5)
    description=models.TextField('Краткое описание')
    category = models.CharField('Категория', max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Десерт"
        verbose_name_plural = "Десерты"