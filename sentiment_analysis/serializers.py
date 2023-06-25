
from rest_framework import serializers


class RequestSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)


class ResponseSerializer(serializers.Serializer):
    sentiment = serializers.CharField()
