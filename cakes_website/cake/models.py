from django.db import models


class PublishedModel(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
    )

    class Meta:
        abstract = True


class Image(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    image = models.ImageField(upload_to='images', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.title


class Category(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Слаг')
    output_order = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='Порядок отображения'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Decoration(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Украшение'
        verbose_name_plural = 'Украшения'

    def __str__(self):
        return self.title


class Cake(PublishedModel):
    is_on_main = models.BooleanField(default=False, verbose_name='На главную')
    title = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    output_order = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='Порядок отображения'
    )
    images = models.ManyToManyField(Image, blank=True,
                                    verbose_name='Изображения')
    price = models.DecimalField(max_digits=8, decimal_places=0,
                                verbose_name='Цена')
    weight = models.DecimalField(max_digits=8, decimal_places=0,
                                 verbose_name='Вес')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='cakes',
        verbose_name='Категория'
    )
    decorations = models.ManyToManyField(Decoration, verbose_name='Украшения')

    class Meta:
        verbose_name = 'Торт'
        verbose_name_plural = 'Торты'
        ordering = ('output_order', 'title')

    def __str__(self):
        return self.title
