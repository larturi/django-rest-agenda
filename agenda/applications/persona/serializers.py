from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Hobby, Person, Reunion

class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = (
            'id',
            'hobby',
        )

class PersonSerializer(serializers.ModelSerializer):

    hobbies = HobbySerializer(many=True)
    class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobbies',
        )

class ReunionSerializer(serializers.ModelSerializer):

    persona = PersonSerializer()
    class Meta:
        model = Reunion
        fields = (
            'id',
            'asunto',
            'fecha',
            'hora',
            'persona',
        )