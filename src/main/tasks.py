import datetime
import logging
import psycopg2
import mysql.connector
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


@app.task
def check_parser_db():
    dbs = ParserDbChecker.objects.all()
    for db in dbs:
        if datetime.timedelta(timezone.now() - db.last_check).seconds // 3600 >= db.check_interval_in_minutes:
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
                sql_request = ParserDbCheckerResult(tablename="Connection error", is_empty=True,
                                                    parser_db=db)
                sql_request.save()
                result = Result(colour="red", description="Не установлено соединение с базой данных",
                                sql_request=sql_request)
                result.save()
