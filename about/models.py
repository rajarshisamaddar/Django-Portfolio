from datetime import date
from django.db import models


class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=555)
