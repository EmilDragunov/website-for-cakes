from django.contrib import admin
from .models import Cake, Image


admin.site.empty_value_display = 'Не задано'


class CakeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_published',
        'is_on_main',
        'price',
        'weight'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'price',
        'weight'
    )
    search_fields = ('title',)
    list_filter = ('title',)
    list_display_links = ('title',)
    filter_horizontal = ('images',)


admin.site.register(Cake, CakeAdmin)
admin.site.register(Image)
