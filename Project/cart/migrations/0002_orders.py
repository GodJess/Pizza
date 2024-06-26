# Generated by Django 4.2.1 on 2023-09-02 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=100, verbose_name='login')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('adress', models.CharField(max_length=100, verbose_name='Адрес доставки')),
                ('price', models.CharField(max_length=100, verbose_name='Цена заказа')),
            ],
            options={
                'verbose_name': 'Заказ1',
                'verbose_name_plural': 'Заказы1',
            },
        ),
    ]
