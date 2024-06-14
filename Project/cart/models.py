from django.db import models



class Order(models.Model):
    login = models.CharField("login", max_length=100)
    name = models.CharField("Имя", max_length=100)
    surname = models.CharField('Фамилия', max_length=100)
    adress =  models.CharField('Адрес доставки', max_length=100)
    price = models.CharField('Цена заказа', max_length=100)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        
class Orders(models.Model):
    login = models.CharField("login", max_length=100)
    name = models.CharField("Имя", max_length=100)
    surname = models.CharField('Фамилия', max_length=100)
    adress =  models.CharField('Адрес доставки', max_length=100)
    price = models.CharField('Цена заказа', max_length=100)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Заказ1"
        verbose_name_plural = "Заказы1"
    
    

