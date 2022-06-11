from django.db import models
from ckeditor.fields import RichTextField


class Subscriber(models.Model):
    email = models.CharField(max_length=55)


class Blog(models.Model):
    title = models.CharField(max_length=150)
    tag1 = models.CharField(max_length=25, blank=True)
    tag2 = models.CharField(max_length=25, blank=True)
    tag3 = models.CharField(max_length=25, blank=True)
    tag4 = models.CharField(max_length=25, blank=True)
    tag5 = models.CharField(max_length=25, blank=True)
    tag6 = models.CharField(max_length=25, blank=True)
    content = RichTextField(blank=True, null=True)
    slug = models.CharField(max_length=150)
    timeStamp = models.DateTimeField(False)
