from django.urls import path

from main.views import test, DatabasesView

urlpatterns = [
    path('', test, name="main"),
    path('databases/', DatabasesView.as_view(), name='databases')
]
