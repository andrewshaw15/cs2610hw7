from django.urls import path

from . import views

app_name = 'webAPI'
urlpatterns = [
    path('', views.index, name='index'),
    path('init/', views.init, name='init'),
]