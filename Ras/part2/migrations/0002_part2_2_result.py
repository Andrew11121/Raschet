# Generated by Django 2.2.7 on 2020-02-21 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='part2_2',
            name='result',
            field=models.CharField(default={models.FloatField(default=1), models.FloatField(default=1)}, max_length=4),
        ),
    ]