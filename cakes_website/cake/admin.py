from django.contrib import admin
from .models import Cake, Category, Decoration


admin.site.empty_value_display = 'Не задано'


class CakeInline(admin.StackedInline):
    model = Cake
    extra = 0
    filter_horizontal = ('decorations',)


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        CakeInline,
    )
    list_display = (
        'title',
    )


class CakeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'price',
        'weight',
        'category'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'price',
        'weight',
        'category'
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)
    filter_horizontal = ('decorations',)


admin.site.register(Cake, CakeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Decoration)

