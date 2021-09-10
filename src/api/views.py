from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from api.serializers import RegisterParserSerializer
from main.models import Parser


class RegisterParserView(CreateAPIView):
    serializer_class = RegisterParserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.create(serializer.validated_data)
            return Response({"status": 201, "name": instance.name, "token": instance.token}, status=201)
        else:
            return Response(serializer.errors, status=400)
