from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'cake'

urlpatterns = [
    path('<int:pk>/', views.cake_detail, name='cake_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
