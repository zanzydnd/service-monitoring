import re

from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.contrib import admin

from main.models import Database, DatabaseFieldsToCheck, Result, DatabaseMonitoring
from main.services.hash_service import jwt_string


class DatabaseForm(ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", cleaned_data['db_ip']):
            raise ValidationError(
                "Incorrect ip address"
            )

    class Meta:
        model = Database
        fields = ['db_name', 'db_ip', 'db_username', 'db_password', 'rmdb']


class CustomAdminDatabase(admin.ModelAdmin):
    form = DatabaseForm


admin.site.register(Database, CustomAdminDatabase)
admin.site.register(DatabaseFieldsToCheck)
admin.site.register(Result)
admin.site.register(DatabaseMonitoring)
