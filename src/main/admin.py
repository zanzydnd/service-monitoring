from django.forms import ModelForm
from django.contrib import admin

from main.models import Database, DatabaseFieldsToCheck, Result, DatabaseMonitoring
from main.services.hash_service import jwt_string


class DatabaseForm(ModelForm):

    def save(self, commit=True):
        database = super(DatabaseForm, self).save(commit=False)
        database.db_password = jwt_string(self.cleaned_data['db_password'])
        if commit:
            database.save()
        return database

    class Meta:
        model = Database
        fields = ['db_name', 'db_ip', 'db_username', 'db_password']


class CustomAdminDatabase(admin.ModelAdmin):
    form = DatabaseForm


admin.site.register(Database, CustomAdminDatabase)
admin.site.register(DatabaseFieldsToCheck)
admin.site.register(Result)
admin.site.register(DatabaseMonitoring)
