from django.shortcuts import render

from rest_framework.generics import ListAPIView

from .models import Person
from .serializers import PersonSerializer

class PersonsListApiView(ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()
