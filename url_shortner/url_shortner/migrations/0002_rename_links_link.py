# Generated by Django 5.1.4 on 2024-12-20 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortner', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Links',
            new_name='Link',
        ),
    ]