

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workouts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=50)),
                ('lat', models.DecimalField(decimal_places=2, max_digits=4)),
                ('lng', models.DecimalField(decimal_places=2, max_digits=4)),
                ('radius', models.DecimalField(decimal_places=2, max_digits=4)),
                ('duration', models.DecimalField(decimal_places=2, max_digits=4)),
                ('distance', models.DecimalField(decimal_places=2, max_digits=4)),
                ('average_hr', models.DecimalField(decimal_places=2, max_digits=4)),
                ('calories_burned', models.DecimalField(decimal_places=2, max_digits=4)),
                ('average_speed', models.DecimalField(decimal_places=2, max_digits=4)),
                ('workout_effectiveness', models.BooleanField()),
            ],
        ),
    ]
