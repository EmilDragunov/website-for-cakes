# Generated by Django 3.2.16 on 2024-06-28 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0005_alter_image_options_cake_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='images',
            field=models.ManyToManyField(blank=True, to='cake.Image', verbose_name='Изображения'),
        ),
    ]
