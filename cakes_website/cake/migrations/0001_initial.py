# Generated by Django 3.2.16 on 2024-06-26 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(max_length=64, unique=True, verbose_name='Слаг')),
                ('output_order', models.PositiveSmallIntegerField(default=100, verbose_name='Порядок отображения')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Decoration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(max_length=64, unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Украшение',
                'verbose_name_plural': 'Украшения',
            },
        ),
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('is_on_main', models.BooleanField(default=False, verbose_name='На главную')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('output_order', models.PositiveSmallIntegerField(default=100, verbose_name='Порядок отображения')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Цена')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cakes', to='cake.category', verbose_name='Категория')),
                ('decorations', models.ManyToManyField(to='cake.Decoration', verbose_name='Украшения')),
            ],
            options={
                'verbose_name': 'Торт',
                'verbose_name_plural': 'Торты',
                'ordering': ('output_order', 'title'),
            },
        ),
    ]
