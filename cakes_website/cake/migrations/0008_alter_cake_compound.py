# Generated by Django 3.2.16 on 2024-07-05 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0007_auto_20240705_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='compound',
            field=models.TextField(default=None, verbose_name='Состав'),
        ),
    ]
