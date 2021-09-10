from django.db import models
from django.utils import timezone


class Parser(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    token = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "parser"
        verbose_name = "Парсер"
        verbose_name_plural = "Парсеры"


class ParserReport(models.Model):
    parser = models.ForeignKey(Parser, on_delete=models.CASCADE, related_name="reports")
    report_date = models.DateTimeField(default=timezone.now, editable=False)
    status = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    class Meta:
        db_table = "parser_report"
        verbose_name = "Отчет от парсера"
        verbose_name_plural = "Отчеты от парсеров"
