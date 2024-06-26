# Generated by Django 4.2.3 on 2023-07-17 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=250, verbose_name='Изображение')),
                ('name', models.CharField(max_length=20, verbose_name='Название пиццы')),
                ('price', models.CharField(max_length=5, verbose_name='price')),
                ('description', models.TextField(verbose_name='Краткое описание')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
