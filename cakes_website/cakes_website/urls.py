from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('homepage.urls')),
    path('cake/', include('cake.urls')),
    path('about/', include('about.urls')),
    path('admin/', admin.site.urls),
]
