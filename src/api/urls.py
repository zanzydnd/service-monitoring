from django.urls import path

from api.views import RegisterParserView

urlpatterns = [
    path("parser/register/", RegisterParserView.as_view(), name="create-parser"),
    #path("parser/report/"),
]
