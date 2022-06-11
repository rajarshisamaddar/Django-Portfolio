from django.contrib import admin

from django.contrib import admin
from home.models import Blog, Subscriber

admin.site.register(Subscriber)

admin.site.register(Blog)
