from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('search', views.search, name='search'),
    path('<str:slug>', views.blog, name='blog'),
]
