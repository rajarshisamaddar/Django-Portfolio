import email
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=1000)


class ContactParagraph(models.Model):
    paragraph = models.CharField(max_length=555)


class ContactFindMe(models.Model):
    location = models.CharField(max_length=555)
    working_time = models.CharField(max_length=555)
    call_me = models.CharField(max_length=555)
    email = models.CharField(max_length=555)
