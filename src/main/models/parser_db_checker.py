from django.db import models


class ParserDbChecker(models.Model):
    DB_VARIANTS = [
        ("My_sql", "My_sql"),
        ("PostgreSQL", "PostgreSQL")
    ]

    parser_name = models.CharField(max_length=1000, unique=True)
    check_interval_in_minutes = models.IntegerField()
    host = models.CharField(max_length=1000)
    database_name = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)
    last_check = models.DateTimeField(null=True, blank=True)
    db_user_name = models.CharField(max_length=100)
    rmdb = models.CharField(choices=DB_VARIANTS, default="PostgreSQL", max_length=100)
    db_port = models.IntegerField(default=5432)

    def __str__(self):
        return self.parser_name

    class Meta:
        db_table = "parser_database"
        verbose_name = "База данных парсера , для проверки работы парсера"
        verbose_name_plural = "Базы данных парсеров , для проверки работы парсеров"


class TablesToCheck(models.Model):
    tablename = models.CharField(max_length=1000)
    parser_db = models.ForeignKey(ParserDbChecker, on_delete=models.CASCADE, related_name="tables_to_check")
    is_empty = models.BooleanField()

    def __str__(self):
        request = ""
        request += "select * from " + str(self.tablename) + " limit 1"
        return request

    class Meta:
        db_table = "table_name_for_parser"
        verbose_name = "Таблица для проверки парсера"
        verbose_name_plural = "Таблицы для проверки парсеров"


class ParserDbCheckerResult(models.Model):
    table = models.ForeignKey(TablesToCheck, on_delete=models.CASCADE, related_name="results")
    status = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)

    class Meta:
        db_table = "parser_databases_result"
