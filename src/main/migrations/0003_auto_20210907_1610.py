# Generated by Django 3.1.7 on 2021-09-07 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210906_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='databasefieldstocheck',
            name='is_empty',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='databasefieldstocheck',
            name='where_statement',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
