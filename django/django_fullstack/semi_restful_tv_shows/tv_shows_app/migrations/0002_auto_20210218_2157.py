# Generated by Django 2.2 on 2021-02-19 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]
