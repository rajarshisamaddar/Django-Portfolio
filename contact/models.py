from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=1000)
