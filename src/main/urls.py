from django.urls import path

from main.views import test, DatabasesView, ParsersView

urlpatterns = [
    path('', test, name="main"),
    path('databases/', DatabasesView.as_view(), name='databases'),
    path("parsers/", ParsersView.as_view(), name='parsers')
]
