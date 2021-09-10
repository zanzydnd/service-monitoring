from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from main.dto import DatabaseDTO, ParserDTO
from main.models import Database, Result, Parser, ParserReport


def test(request):
    return render(request, "main.html")


class DatabasesView(ListView):
    template_name = "databases.html"
    context_object_name = "databases"
    model = Database

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = Database.objects.all()
        result_queryset = []
        for database in qs:
            results = Result.objects.filter(sql_request__data_base__id=database.id).order_by("-date")[:90]
            dto = DatabaseDTO(database=database, last_results=results)
            result_queryset.append(dto)
        context['database_dto'] = result_queryset
        return context


class ParsersView(ListView):
    template_name = "parsers.html"
    context_object_name = "parsers"
    model = Parser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = Parser.objects.all()
        result_queryset = []
        for parser in qs:
            reports = ParserReport.objects.filter(parser=parser).order_by("-report_date")[:90]
            dto = ParserDTO(parser=parser, last_reports=reports)
            result_queryset.append(dto)
        context['parser_dto'] = result_queryset
        return context
