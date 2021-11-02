from django.shortcuts import render

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView
)

from .models import Person, Reunion
from .serializers import (
    PersonSerializer,
    ReunionSerializer
)

class PersonsListApiView(ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()

class PersonsSearchListApiView(ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        kword = self.kwargs['kword']
        return Person.objects.filter(
            full_name__icontains=kword
        )
class PersonCreateApiView(CreateAPIView):
    serializer_class = PersonSerializer

class PersonDetailApiView(RetrieveAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonDeleteApiView(DestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonUpdateApiView(RetrieveUpdateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonApiView(ListAPIView):
    # Vista para interactuar con serializer 
    serializer_class = PersonSerializer
    
    def get_queryset(self):
        return Person.objects.all()

class ReunionApiView(ListAPIView):
    serializer_class = ReunionSerializer
    
    def get_queryset(self):
        return Reunion.objects.all()