from django.shortcuts import get_object_or_404, render
from cake.models import Cake


def cake_detail(request, pk):
    template = 'cake/detail.html'
    cake = get_object_or_404(
        Cake.objects.filter(
            is_published=True,
        ),
        pk=pk
    )
    context = {
        'cake': cake
    }
    return render(request, template, context)
