# Generated by Django 2.1.3 on 2018-12-10 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_image_image_small'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_small',
        ),
    ]
