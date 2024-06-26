from django.urls import path

from . import views

app_name = 'cake'

urlpatterns = [
    path('', views.cake_list, name='cake_list'),
    path('<int:pk>/', views.cake_detail, name='cake_detail'),
]
