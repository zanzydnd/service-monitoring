from django.db import models


class Database(models.Model):
    db_name = models.CharField(max_length=250)
    db_ip = models.CharField(max_length=13)
    db_username = models.CharField(max_length=300)
    db_password = models.CharField(max_length=300)

    class Meta:
        db_table = "_database_"
        verbose_name = "База для проверки"
        verbose_name_plural = "Базы для проверок"

    def __str__(self):
        return self.db_name


class DatabaseFieldsToCheck(models.Model):
    # type = select, insert
    table_name_to_check = models.CharField(max_length=200)
    where_statement = models.CharField(max_length=100)
    data_base = models.ForeignKey(Database, on_delete=models.CASCADE, related_name="sql_requests_to_check")

    class Meta:
        db_table = "database_sql_requests_constructor"
        verbose_name = "Запрос, который будет проверяться."
        verbose_name_plural = "Запросы, которые будут проверяться."


class Result(models.Model):
    colour = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    class Meta:
        db_table = "sql_request_result"
        verbose_name = "Результат Запроса"
        verbose_name_plural = "Результаты Запросов"


class DatabaseMonitoring(models.Model):
    sql_request = models.ForeignKey(DatabaseFieldsToCheck, on_delete=models.DO_NOTHING,
                                    related_name="sql_request_results")
    result = models.ForeignKey(Result, on_delete=models.CASCADE, related_name="sql_requests")
    date = models.DateField(auto_now=True)

    class Meta:
        db_table = "sql_request"
        verbose_name = "Запрос в базу данных(выполненный)"
        verbose_name_plural = "Запросы в базу данных(выполненные)"
