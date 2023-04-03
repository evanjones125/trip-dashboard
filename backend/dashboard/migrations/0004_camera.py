# Generated by Django 4.1.7 on 2023-04-03 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_location_longitude'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=120)),
                ('agency', models.CharField(default='agency', max_length=120)),
                ('latitude', models.DecimalField(decimal_places=6, default=0.0, max_digits=8)),
                ('longitude', models.DecimalField(decimal_places=6, default=0.0, max_digits=9)),
                ('url', models.CharField(default='null', max_length=120)),
            ],
        ),
    ]
