from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 

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
        'description': 'Delete an exisitng Note'
    },
    
    
    
     ]
    return Response(routes)