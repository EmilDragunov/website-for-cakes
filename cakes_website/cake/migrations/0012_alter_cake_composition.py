# Generated by Django 3.2.16 on 2024-07-05 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0011_rename_compound_cake_composition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='composition',
            field=models.CharField(max_length=500, verbose_name='Состав'),
        ),
    ]
