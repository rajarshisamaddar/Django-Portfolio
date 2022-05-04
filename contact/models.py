import email
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=75)
    email = models.CharField(max_length=55)
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=2000)


class ContactParagraph(models.Model):
    paragraph = models.CharField(max_length=1200)


class ContactFindMe(models.Model):
    location = models.CharField(max_length=105)
    working_time = models.CharField(max_length=105)
    call_me = models.CharField(max_length=105)
    email = models.CharField(max_length=105)
