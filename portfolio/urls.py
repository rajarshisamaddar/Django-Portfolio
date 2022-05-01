from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('work/', include('work.urls')),
    path('contact/', include('contact.urls')),
    path('root/', admin.site.urls),
]
