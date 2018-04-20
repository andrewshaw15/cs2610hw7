from django.urls import path

from . import views

app_name = 'simplePage'
urlpatterns = [
    path('', views.index, name='index'),
]