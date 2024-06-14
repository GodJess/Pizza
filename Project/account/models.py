from django.db import models

# Create your models here.
class User(models.Model):
    login = models.CharField("Логин", max_length=50)
    mail = models.CharField("Почта", max_length=50)
    password = models.CharField("Пароль", max_length=50)

    def __str__(self):
        return self.login
    

    class Meta:
        verbose_name = "Пользватель"
        verbose_name_plural = "Пользователи"