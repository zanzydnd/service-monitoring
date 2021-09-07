from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from main.dto import DatabaseDTO
from main.models import Database, Result


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
            results = Result.objects.filter(sql_request__data_base__id=database.id).order_by("date")[:90]
            dto = DatabaseDTO(database=database, last_results=results)
            result_queryset.append(dto)
        context['database_dto'] = result_queryset
        return context


