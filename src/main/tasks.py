import logging
import psycopg2

from main.models import Database, Result, DatabaseFieldsToCheck
from main.services.database_service import postgreSql_execute_request
from service_monitoring.celery import app

logger = logging.getLogger(__name__)


@app.task
def check_databases():
    databases = Database.objects.all()
    for database in databases:
        if database.rmdb == "PostgreSQL":
            try:
                conn = psycopg2.connect(dbname=database.db_name, user=database.db_username,
                                        password=database.db_password, host=database.db_ip)
                postgreSql_execute_request(conn, database)
            except psycopg2.OperationalError as e:
                print(e)
                sql_request = DatabaseFieldsToCheck(table_name_to_check="Connection error", is_empty=True,
                                                    data_base=database)
                sql_request.save()
                result = Result(colour="red", description="Не установлено соединение с базой данных",
                                sql_request=sql_request)
                result.save()
        elif database.rmdb == "My_sql":
            pass
