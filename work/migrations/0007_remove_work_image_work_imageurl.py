# Generated by Django 4.0.3 on 2022-06-11 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0006_work_file_name_work_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='image',
        ),
        migrations.AddField(
            model_name='work',
            name='imageUrl',
            field=models.CharField(default='', max_length=1500),
            preserve_default=False,
        ),
    ]
