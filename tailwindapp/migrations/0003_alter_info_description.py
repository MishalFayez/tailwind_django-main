# Generated by Django 4.1.2 on 2022-10-30 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tailwindapp', '0002_info_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
