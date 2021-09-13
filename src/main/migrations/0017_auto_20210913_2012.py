# Generated by Django 3.1.7 on 2021-09-13 17:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_parserdbcheckerresult_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablestocheck',
            name='is_empty',
        ),
        migrations.AlterField(
            model_name='parserdbcheckerresult',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]