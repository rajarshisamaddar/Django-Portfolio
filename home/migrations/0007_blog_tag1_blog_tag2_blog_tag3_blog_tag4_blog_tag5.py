# Generated by Django 4.0.3 on 2022-06-10 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tag1',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='blog',
            name='tag2',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='blog',
            name='tag3',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='blog',
            name='tag4',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='blog',
            name='tag5',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
