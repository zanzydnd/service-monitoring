import traceback

import psycopg2

from main.models import Result, DatabaseMonitoring


def postgreSql_execute_request(conn, database, requests):
    for request in requests:
        try:
            print(request[0])
            with conn.cursor() as cursor:
                cursor.execute(request[0])
            result = Result(colour="#2fcc66", description="Ok")
            result.save()
            monitor = DatabaseMonitoring(result=result, sql_request=request[1])
            monitor.save()
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as e:
            conn.rollback()
            traceback.print_exc()
            result = Result(colour="orange", description=str(e))
            result.save()
            monitor = DatabaseMonitoring(result=result, sql_request=request[1])
            monitor.save()
    conn.close()

def postgreSql_make_request(conn, database):
    requests_combined = []

    for request_raw in database.sql_requests_to_check.all():
        if request_raw.is_empty:
            continue
        request = "" + request_raw.type
        if request_raw.type == "select":
            request += " * from " + request_raw.table_name_to_check
            if request_raw.where_statement:
                request += " where " + request_raw.where_statement
            request += " limit 3"
            requests_combined.append((request, request_raw))
        else:
            pass

    postgreSql_execute_request(conn, database, requests_combined)
