from django.contrib import admin
from django.urls import path, re_path, include

from .views import (
    PersonCreateApiView,
    PersonDeleteApiView, 
    PersonDetailApiView, 
    PersonsListApiView, 
    PersonsSearchListApiView
)

app_name = 'person_app'

urlpatterns = [
    path('api/person/list/', PersonsListApiView.as_view()),
    path('api/person/search/<kword>/', PersonsSearchListApiView.as_view()),
    path('api/person/create/', PersonCreateApiView.as_view()),
    path('api/person/detail/<pk>/', PersonDetailApiView.as_view()),
    path('api/person/delete/<pk>/', PersonDeleteApiView.as_view()),
]
