from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView

from main.models import Database


def test(request):
    return render(request, "main.html")


class DatabasesView(ListView):
    template_name = "databases.html"
    context_object_name = "databases"
    model = Database

    def get_context_data(self, *, object_list=None, **kwargs):
        pass

    #def get_queryset(self):
        #results =
        #qs = Database.objects.all().select_related("sql_requests_to_check__sql_requests")
        #return qs