# Generated by Django 3.1.7 on 2021-09-08 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210908_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='database',
            name='db_port',
            field=models.IntegerField(default=5432),
        ),
    ]