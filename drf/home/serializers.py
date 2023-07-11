from rest_framework import serializers


class PersonSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    married = serializers.BooleanField()