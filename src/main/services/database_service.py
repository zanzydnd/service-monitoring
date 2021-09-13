import traceback

import psycopg2

from main.models import Result


def sql_execute_request(conn, database):
    for request in database.sql_requests_to_check.all():
        if request.is_empty:
            continue
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


def parser_database_check(conn, parser_database):
    for request in parser_database.tables_to_check.all():
        if request.is_empty:
            continue
        try:
            if parser_database.rmdb == "My_sql":
                with conn.cursor(buffered=True) as cursor:
                    element = cursor.execute(str(request))
            else:
                with conn.cursor() as cursor:
                    element = cursor.execute(str(request))
            if not request.result:
                request.result = ''.join(element)
            else:
                new = ''.join(element)
                if new != request.result:
                    request.result = new
                    # сохранить со статусом ok
                else:
                    # сохранить со статусом not_critical
                    pass
            request.save()
            conn.commit()
            print(element)
        except (Exception, psycopg2.DatabaseError) as e:
            conn.rollback()
            traceback.print_exc()
            # сохранить со статусом critical.
    conn.close()
