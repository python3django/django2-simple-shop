# Generated by Django 2.1.3 on 2018-12-08 12:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20181208_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default='', max_length=15, validators=[django.core.validators.RegexValidator(message="Введите украинский телефонный номер в формате код оператора + номер телефона: '0671234567'. От 10 до 15 цифр.", regex='^\\d{10,15}$')]),
        ),
    ]
