# Generated by Django 3.2.16 on 2024-07-05 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0013_remove_cake_composition'),
    ]

    operations = [
        migrations.AddField(
            model_name='cake',
            name='composition',
            field=models.TextField(default='', verbose_name='Состав'),
        ),
    ]
