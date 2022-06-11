from django.db import models


class Work(models.Model):
    imageUrl = models.CharField(max_length=1500)
    file_name = models.CharField(max_length=255)
    tag1 = models.CharField(max_length=55, blank=True)
    tag2 = models.CharField(max_length=55, blank=True)
    tag3 = models.CharField(max_length=55, blank=True)
    tag4 = models.CharField(max_length=55, blank=True)
    tag5 = models.CharField(max_length=55, blank=True)
    tag6 = models.CharField(max_length=55, blank=True)
    title = models.CharField(max_length=255)
    startDate = models.CharField(max_length=55)
    endDate = models.CharField(max_length=55)
    description = models.CharField(max_length=1200)
    github = models.CharField(max_length=155)


class Resume(models.Model):
    resume = models.FileField(upload_to='django-portfolio\www\public/resume')
