import logging
import psycopg2

from main.models import Database
from main.services.database_service import postgreSql_make_request
from service_monitoring.celery import app

logger = logging.getLogger(__name__)


@app.task(queue="default")
def check_databases():
    databases = Database.objects.all()
    for database in databases:
        if database.rmdb == "PostgreSQL":
            conn = psycopg2.connect(dbname=database.db_name, user=database.db_username,
                                    password=database.db_password, host=database.db_ip)
            result = postgreSql_make_request(conn.cursor(), database)
            conn.close()
        elif database.rmdb == "My_sql":
            pass
