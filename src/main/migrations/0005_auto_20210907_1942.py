# Generated by Django 3.1.7 on 2021-09-07 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210907_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]