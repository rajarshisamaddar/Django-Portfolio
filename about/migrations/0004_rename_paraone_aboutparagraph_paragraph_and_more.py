# Generated by Django 4.0.3 on 2022-05-04 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_rename_aboutparagraphs_aboutparagraph_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutparagraph',
            old_name='paraone',
            new_name='paragraph',
        ),
        migrations.RemoveField(
            model_name='aboutparagraph',
            name='parathree',
        ),
        migrations.RemoveField(
            model_name='aboutparagraph',
            name='paratwo',
        ),
    ]