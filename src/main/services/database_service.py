import traceback

import psycopg2
from django.utils import timezone

from main.models import Result, ParserDbCheckerResult


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
        try:
            print(request)
            if parser_database.rmdb == "My_sql":
                with conn.cursor(buffered=True) as cursor:
                    cursor.execute(str(request))
                    element = cursor.fetchall()[0]
            else:
                with conn.cursor() as cursor:
                    cursor.execute(str(request))
                    element = cursor.fetchall()[0]
            print(element)
            element = [str(i) for i in element if i]
            if not request.result:
                request.result = ''.join(element)
                res = ParserDbCheckerResult(table=request, status="ok", description="First saving")
                res.save()
            else:
                new = ''.join(element)
                if new != request.result:
                    request.result = new
                    res = ParserDbCheckerResult(table=request, status="ok", description="Ok")
                    res.save()
                else:
                    res = ParserDbCheckerResult(table=request, status="not_critical",
                                                description="Не обновилась запись.")
                    res.save()
            request.save()
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as e:
            conn.rollback()
            traceback.print_exc()
            res = ParserDbCheckerResult(table=request, status="critical",
                                        description=str(e))
            res.save()
    parser_database.last_check = timezone.now()
    parser_database.save()
    conn.close()
