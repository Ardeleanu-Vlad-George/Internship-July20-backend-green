# Generated by Django 3.0.8 on 2020-07-17 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200716_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
    ]