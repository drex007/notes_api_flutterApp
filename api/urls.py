
from django.contrib import admin
from django.urls import path, include
from .views import getRoutes,getNotes, createNote, getNote, updateNote, deleteNote


urlpatterns = [
   
    path('', getRoutes, name="getRoutes"),
    path('notes/', getNotes, name="getNotes"),
    path('notes/<int:pk>/', getNote, name="getNote"),
    path('notes/create/', createNote, name="=createNote"),
    path('notes/<int:pk>/update', updateNote, name="=updateNote"),
    path('notes/<int:pk>/delete', deleteNote, name="=deleteNote"),
]
