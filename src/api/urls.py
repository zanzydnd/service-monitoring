from django.urls import path, re_path

from api.views import RegisterParserView, ReportParserView


urlpatterns = [
    path("parser/register/", RegisterParserView.as_view(), name="create-parser"),
    path("parser/report/<str:name>", ReportParserView.as_view(), name="report-parser"),
]
