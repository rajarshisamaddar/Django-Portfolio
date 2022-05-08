from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('error', views.error, name='error'),
    path('message', views.message, name='message'),
]
