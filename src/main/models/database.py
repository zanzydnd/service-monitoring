from django.db import models
from django.utils import timezone


class Database(models.Model):
    DB_VARIANTS = [
        ("My_sql", "My_sql"),
        ("PostgreSQL", "PostgreSQL")
    ]

    db_name = models.CharField(max_length=250)
    db_ip = models.CharField(max_length=100)
    db_username = models.CharField(max_length=300)
    db_password = models.CharField(max_length=300)
    rmdb = models.CharField(choices=DB_VARIANTS, default="PostgreSQL", max_length=100)
    db_port = models.IntegerField(default=5432)

    class Meta:
        db_table = "_database_"
        verbose_name = "База для проверки"
        verbose_name_plural = "Базы для проверок"

    def __str__(self):
        return self.db_name


class DatabaseFieldsToCheck(models.Model):
    SQL_TYPES = [
        ("select", "select"),
        ("insert", "insert")
    ]

    type = models.CharField(max_length=100, choices=SQL_TYPES, default="select")
    table_name_to_check = models.CharField(max_length=200)
    where_statement = models.CharField(max_length=100, null=True, blank=True)
    data_base = models.ForeignKey(Database, on_delete=models.CASCADE, related_name="sql_requests_to_check")
    is_empty = models.BooleanField(default=False)

    class Meta:
        db_table = "database_sql_requests_constructor"
        verbose_name = "Запрос, который будет проверяться."
        verbose_name_plural = "Запросы, которые будут проверяться."

    def __str__(self):
        if self.is_empty:
            return "Empty request"
        request = "" + str(self.type)
        if self.type == "select":
            request += " * from " + str(self.table_name_to_check)
            if self.where_statement:
                request += " where " + str(self.where_statement)
            request += " limit 3"
        else:
            pass
        return request


class Result(models.Model):
    colour = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    date = models.DateTimeField(default=timezone.now, editable=False)
    sql_request = models.ForeignKey(DatabaseFieldsToCheck, on_delete=models.CASCADE, related_name="results",
                                    default=None)

    class Meta:
        db_table = "sql_request_result"
        verbose_name = "Результат Запроса"
        verbose_name_plural = "Результаты Запросов"
