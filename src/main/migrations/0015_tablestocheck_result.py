# Generated by Django 3.1.7 on 2021-09-13 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210913_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablestocheck',
            name='result',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
