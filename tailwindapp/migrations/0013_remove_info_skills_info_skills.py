# Generated by Django 4.1.2 on 2022-11-07 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tailwindapp', '0012_remove_info_skills_info_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='skills',
        ),
        migrations.AddField(
            model_name='info',
            name='skills',
            field=models.ManyToManyField(to='tailwindapp.skills'),
        ),
    ]
