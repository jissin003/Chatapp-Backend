from . import views
from django.urls import path,include
from django.contrib import admin

urlpatterns=[
    path('',views.rooms),
    path("<str:slug>/",views.room)
]