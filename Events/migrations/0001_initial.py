<<<<<<< HEAD
# Generated by Django 3.0.8 on 2020-07-23 12:53
=======
# Generated by Django 3.0.8 on 2020-07-23 08:48
>>>>>>> 4dc920873052c577dd63e80ebe66c9dfd0bea68c

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clubs', '0001_initial'),
        ('Sports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=50)),
                ('location', models.CharField(max_length=30)),
                ('radius', models.CharField(max_length=30)),
<<<<<<< HEAD
                ('Date_Time', models.DateTimeField(auto_now_add=True)),
=======
>>>>>>> 4dc920873052c577dd63e80ebe66c9dfd0bea68c
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clubs.Clubs')),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sports.Sports')),
            ],
        ),
    ]
