
from django.contrib import admin
from django.urls import path, include
from .views import getRoutes


urlpatterns = [
   
    path('', getRoutes, name="getRoutes"),
]
