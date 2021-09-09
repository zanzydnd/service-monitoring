import traceback

import psycopg2

from main.models import Result


def postgreSql_execute_request(conn, database):
    for request in database.sql_requests_to_check.all():
        try:
            if database.rmdb == "My_sql":
                with conn.cursor(buffered=True) as cursor:
                    cursor.execute(str(request))
            else:
                with conn.cursor() as cursor:
                    cursor.execute(str(request))
            result = Result(colour="#2fcc66", description="Ok", sql_request=request)
            result.save()
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as e:
            conn.rollback()
            traceback.print_exc()
            result = Result(colour="orange", description=str(e), sql_request=request)
            result.save()
    conn.close()
