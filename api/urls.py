
from django.contrib import admin
from django.urls import path, include
from .views import getRoutes,getNotes, createNote, getNote, updateNote, deleteNote


urlpatterns = [
   
    path('', getRoutes, name="getRoutes"),
    path('notes/', getNotes, name="getNotes"),
    path('note/<int:pk>/', getNote, name="getNote"),
    path('note/create/', createNote, name="=createNote"),
    path('note/update/<int:pk>/', updateNote, name="=updateNote"),
    path('note/delete/<int:pk>/', deleteNote, name="=deleteNote"),
]
