import datetime
import logging
import psycopg2
import mysql.connector
from django.db import models
from django.utils import timezone

from main.models import Database, Result, DatabaseFieldsToCheck, ParserDbChecker, ParserDbCheckerResult
from main.services.database_service import sql_execute_request, parser_database_check
from service_monitoring.celery import app

logger = logging.getLogger(__name__)

@app.task
def check_databases():
    databases = Database.objects.all()
    for database in databases:
        try:
            if database.rmdb == "PostgreSQL":
                conn = psycopg2.connect(dbname=database.db_name, user=database.db_username,
                                        password=database.db_password, host=database.db_ip, port=database.db_port)
            else:
                conn = mysql.connector.connect(database=database.db_name, host=database.db_ip,
                                               user=database.db_username, port=database.db_port,
                                               password=database.db_password)
            sql_execute_request(conn, database)
        except (psycopg2.OperationalError, Exception) as e:
            print(e)
            sql_request = DatabaseFieldsToCheck(table_name_to_check="Connection error", is_empty=True,
                                                data_base=database)
            sql_request.save()
            result = Result(colour="red", description="Не установлено соединение с базой данных",
                            sql_request=sql_request)
            result.save()


SECONDS_IN_DAY = 24 * 60 * 60


@app.task
def check_parser_db():
    dbs = ParserDbChecker.objects.all()
    for db in dbs:
        if db.last_check:
            time__ = (timezone.now() - db.last_check)
        if db.last_check is None or (
                time__.seconds + time__.days * SECONDS_IN_DAY) // 60 >= db.check_interval_in_minutes:
            try:
                if db.rmdb == "PostgreSQL":
                    conn = psycopg2.connect(dbname=db.database_name, user=db.db_user_name,
                                            password=db.password, host=db.host, port=db.db_port)
                else:
                    conn = mysql.connector.connect(database=db.database_name, user=db.db_user_name,
                                                   password=db.password, host=db.host, port=db.db_port)
                parser_database_check(conn, db)
            except (psycopg2.OperationalError, Exception) as e:
                print(e)
                results_ = []
                for table in db.tables_to_check.all():
                    sql_request = ParserDbCheckerResult(table=table, status="critical",
                                                        description="Нет подключения к бд.")
                    results_.append(sql_request)
                db.last_check = timezone.now()
                db.save()
                ParserDbCheckerResult.objects.bulk_create(results_)
