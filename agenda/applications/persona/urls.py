from django.contrib import admin
from django.urls import path, re_path, include

from .views import (
    PersonCreateApiView,
    PersonDeleteApiView, 
    PersonDetailApiView,
    PersonUpdateApiView, 
    PersonsListApiView, 
    PersonsSearchListApiView,
    PersonApiView,
    # 
    ReunionApiView,
    # 
    HobbyDetailApiView,
    ReunionByJob,
)

app_name = 'person_app'

urlpatterns = [
    path('api/person/list/', PersonsListApiView.as_view()),
    path('api/person/search/<kword>/', PersonsSearchListApiView.as_view()),
    path('api/person/create/', PersonCreateApiView.as_view()),
    path('api/person/detail/<pk>/', PersonDetailApiView.as_view(), name='person_detail'),
    path('api/person/delete/<pk>/', PersonDeleteApiView.as_view()),
    path('api/person/update/<pk>/', PersonUpdateApiView.as_view()),
    # 
    path('api/personas/', PersonApiView.as_view()),
    # 
    path('api/hobbies/detail/<pk>/', HobbyDetailApiView.as_view()),
    # 
    path('api/reuniones/list/', ReunionApiView.as_view()),
    path('api/reuniones/job/', ReunionByJob.as_view()),
]
