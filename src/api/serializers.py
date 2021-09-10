from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from main.models import Parser


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
