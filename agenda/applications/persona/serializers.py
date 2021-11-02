from django.db import models
from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
# Serializer basado en modelo
    class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
        )

class PersonaSerializer(serializers.Serializer):
# Serializer no basado en modelo
    class Meta:
        id = serializers.IntegerField()
        full_name = serializers.CharField()
        job = serializers.CharField()
        email = serializers.EmailField()
        phone = serializers.CharField()