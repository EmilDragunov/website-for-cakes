from django.shortcuts import render
from cake.models import Cake
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    template = 'homepage/index.html'
    cake_list = Cake.objects.all().filter(
        is_published=True,
        is_on_main=True
    ).order_by('title')
    paginator = Paginator(cake_list, 100)
    page_number = request.GET.get('page')
    try:
        cakes = paginator.page(page_number)
    except PageNotAnInteger:
        cakes = paginator.page(1)
    except EmptyPage:
        cakes = paginator.page(paginator.num_pages)

    context = {
        'cake_list': cakes,
        'paginator': paginator
    }
    return render(request, template, context)
