from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('message', views.message, name='message'),
]
