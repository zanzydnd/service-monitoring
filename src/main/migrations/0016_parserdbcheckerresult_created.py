# Generated by Django 3.1.7 on 2021-09-13 16:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_tablestocheck_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='parserdbcheckerresult',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
