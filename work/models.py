from datetime import date
from django.db import models


class Work(models.Model):
    type = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    startDate = models.CharField(max_length=255)
    endDate = models.CharField(max_length=255)
    description = models.CharField(max_length=555)
    github = models.CharField(max_length=255)
