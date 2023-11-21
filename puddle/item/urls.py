from django.urls import path

from . import views

app_name = 'item'

urlspatterns = [
    path('<int:pk>/', views.detail, name='detail'),
]