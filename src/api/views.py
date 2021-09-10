from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from api.serializers import RegisterParserSerializer, ReportParserSerializer
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


class ReportParserView(CreateAPIView):
    serializer_class = ReportParserSerializer

    def create(self, request, *args, **kwargs):
        name = kwargs['name']
        request.data['name'] = name
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response({"status": 201}, status=201)
        else:
            return Response(serializer.errors, status=400)
