from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import Note
from .serializers import NoteSerializer



@api_view(['GET'])
def getRoutes(request):
    routes = [ {
        'Endpoint' : '/notes/',
        'method' :'GET',
        'body' : None, 
        'description': 'Return an array of objects'
    },
    {
        'Endpoint' : '/notes/id',
        'method' :'GET',
        'body' : None, 
        'description': 'Return a single notes object'
    },
    {
        'Endpoint' : '/notes/create/',
        'method' :'POST',
        'body' : {'body': ""}, 
        'description': 'Creates a new Note'
    },
    {
        'Endpoint' : '/notes/id/update',
        'method' :'PUT',
        'body' : {'body': ""}, 
        'description': 'Creates an exisiting  note with data sent to the db '
    },
    {
        'Endpoint' : '/notes/id/delete',
        'method' :'DELETE',
        'body' : None, 
        'description': ' To Delete an exisitng Note'
    },
    
    
    
     ]
    return Response(routes)


# Get all the notes
@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serialized = NoteSerializer(notes, many= True)
    return Response(serialized.data)

# Get all the Singlenote
@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id = pk)
    serialized = NoteSerializer(note, many= False)
    return Response(serialized.data)

# Create a Note
@api_view(['POST'])
def createNote(request):
    data = request.data 
    newdata = Note.objects.create(
        body = data['body']
    )
    serialized = NoteSerializer(newdata, many= False)
    return Response(serialized.data)

#Update a note 
@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data 
    note = Note.objects.get(id=pk)
    serialized = NoteSerializer(note, data = data)
    if serialized.is_valid():
        serialized.save()
    return Response(serialized.data)


#Delete a Note when called 
@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Note is  deleted")
 
