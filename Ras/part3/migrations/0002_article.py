# Generated by Django 3.0.3 on 2020-02-14 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('article_heading', models.CharField(max_length=250)),
                ('article_body', models.TextField()),
            ],
        ),
    ]
