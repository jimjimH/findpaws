# Generated by Django 3.0.5 on 2020-04-22 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_animal_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='body_size',
            field=models.CharField(choices=[('A', '0-3kg'), ('B', '3-13kg'), ('C', '13-23kg'), ('D', '23kg+')], max_length=3),
        ),
    ]