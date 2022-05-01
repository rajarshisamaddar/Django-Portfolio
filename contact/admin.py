from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Contact

# Register your models here.
admin.site.site_header = 'ignorecrowd.co.in administration'
admin.site.site_title = "ignorecrowd"
admin.site.index_title = "Rajarshi's envelope"
admin.site.register(Contact)
admin.site.unregister(Group)
