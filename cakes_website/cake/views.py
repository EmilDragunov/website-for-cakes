from django.shortcuts import get_object_or_404, render
from cake.models import Cake


def cake_detail(request, pk):
    template = 'cake/detail.html'
    cake = get_object_or_404(
        Cake.objects.filter(
            is_published=True,
            category__is_published=True
        ),
        pk=pk
    )
    context = {
        'cake': cake
    }
    return render(request, template, context)


def cake_list(request):
    template = 'cake/list.html'
    cake_list = Cake.objects.select_related('category').filter(
        is_published=True,
        category__is_published=True
    ).order_by('category')
    context = {'cake_list': cake_list}
    return render(request, template, context)
