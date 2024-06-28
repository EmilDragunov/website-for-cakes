from django.shortcuts import render
from cake.models import Cake


def index(request):
    template = 'homepage/index.html'
    cake_list = Cake.objects.all().filter(
        is_published=True,
        is_on_main=True,
        category__is_published=True
    )
    context = {
        'cake_list': cake_list,
    }
    return render(request, template, context)
