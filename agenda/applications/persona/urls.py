from django.contrib import admin
from django.urls import path, re_path, include

from .views import PersonsListApiView, PersonsSearchListApiView

app_name = 'person_app'

urlpatterns = [
    path('api/person/list/', PersonsListApiView.as_view(), name='persons'),
    path('api/person/search/<kword>/', PersonsSearchListApiView.as_view()),
]
