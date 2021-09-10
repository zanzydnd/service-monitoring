from django.contrib.auth.hashers import make_password
from django.db import models
from rest_framework import serializers

from main.models import Parser, ParserReport


class RegisterParserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        name = validated_data['name']
        token = make_password(validated_data['name'])
        parser_instance = Parser(name=name, token=token)
        parser_instance.save()
        return parser_instance

    class Meta:
        model = Parser
        fields = ['name']


class ReportParserSerializer(serializers.ModelSerializer):
    token = serializers.CharField()
    name = serializers.CharField()

    def validate(self, data):
        try:
            self.parser = Parser.objects.get(name=data['name'])
            if self.parser.token != data['token']:
                raise serializers.ValidationError("Bad credentials.")
            return data
        except models.ObjectDoesNotExist as e:
            raise serializers.ValidationError("Нет такого имени.")

    def create(self, validated_data):
        descr = validated_data['description']
        status = validated_data['status']
        instance = ParserReport(parser=self.parser, description=descr, status=status)
        instance.save()
        return instance

    class Meta:
        model = ParserReport
        fields = ['status', 'description', 'token', 'name']
