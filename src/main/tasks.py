import logging
import psycopg2

from main.models import Database, Result, DatabaseMonitoring, DatabaseFieldsToCheck
from main.services.database_service import postgreSql_make_request
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
                postgreSql_make_request(conn.cursor(), database)
                conn.close()
            except psycopg2.OperationalError as e:
                result = Result(colour="red", description="Не установлено соединение с базой данных")
                result.save()
                sql_request = DatabaseFieldsToCheck(table_name_to_check="Connection error", is_empty=True,
                                                    data_base=database)
                sql_request.save()
                monitor = DatabaseMonitoring(result=result, sql_request=sql_request)
                monitor.save()
        elif database.rmdb == "My_sql":
            pass
