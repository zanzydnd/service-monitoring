# Generated by Django 3.1.7 on 2021-09-06 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='database',
            name='rmdb',
            field=models.CharField(choices=[('My_sql', 'My_sql'), ('PostgreSQL', 'PostgreSQL')], default='PostgreSQL', max_length=100),
        ),
        migrations.AddField(
            model_name='databasefieldstocheck',
            name='type',
            field=models.CharField(choices=[('select', 'select'), ('insert', 'insert')], default='select', max_length=100),
        ),
    ]