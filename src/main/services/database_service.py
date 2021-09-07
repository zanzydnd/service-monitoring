from main.models import Result, DatabaseMonitoring
import psycopg2


def postgreSql_execute_request(cursor, database, requests):
    for request in requests:
        try:
            cursor.execute(request[0])
            result = Result(colour="#2fcc66", description="Ok")
            result.save()
            monitor = DatabaseMonitoring(result=result, sql_request=request[1])
            monitor.save()
        except psycopg2.Error as e:
            result = Result(colour="red", description=e.pgerror)
            result.save()
            monitor = DatabaseMonitoring(result=result, sql_request=request[1])
            monitor.save()


def postgreSql_make_request(cursor, database):
    requests_combined = []

    for request_raw in database.sql_requests_to_check.all():
        request = "" + request_raw.type
        if request_raw.type == "select":
            request += " * from " + request_raw.table_name_to_check
            if request_raw.where_statement:
                request += " where " + request_raw.where_statement
            request += " limit 3"
            requests_combined.append((request, request_raw))
        else:
            pass

    postgreSql_execute_request(requests_combined)
