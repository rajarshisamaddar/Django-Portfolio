from django.db import models


class AboutParagraph(models.Model):
    paragraph = models.CharField(max_length=555)


class AboutSkill(models.Model):
    skill_left_name = models.CharField(max_length=50)
    skill_left_value = models.CharField(max_length=8)
    skill_right_name = models.CharField(max_length=50)
    skill_right_value = models.CharField(max_length=8)


class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=555)
