from django.http import JsonResponse
from django.shortcuts import render
from .models import Guest, Movie, Reservation
from rest_framework.decorators import api_view
from .serializers import GeustSerializer,MovieSerializer,ReservationSerializer
from tikets import serializers
from rest_framework.response import Response
from rest_framework import status , filters


#1 methode without rest and no model 


def no_rest_no_model(request):


    guests = [

    {
        'id': 1,
        "Name": "Oumar",
        "mobile": "78934",
    },
    { 
        "id": 2,
        "Name": "babah",
        "mobile": 34354   
    }
    ]
    return JsonResponse (guests, safe=False)


#2 methode model data defoult django without rest

def no_rest_from_model(request):

    data =  Guest.objects.all()
    response = {
        'guests': list(data.values('name', 'mobile'))

    }

    return JsonResponse(response)


#3 methode function based views
#3.1  GET POST
@api_view(['GET', 'POST'])
def FBV_List(request):
    
    #GET
    if request.method == 'GET':
        geust = Guest.objects.all()
        serializers = GeustSerializer(geust, many=True)
        return Response(serializers.data)
    
    #POST
    elif request.method == 'POST':
        serializer = GeustSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    



#3.2 GET PUT ET DELATE
@api_view(['GET','PUT', 'DELETE'])
def FBV_pk(request, pk):
 try:
    geust = Guest.objects.get(pk=pk)
 
    #GET
    if request.method == 'GET':
        serializers = GeustSerializer(geust)
        return Response(serializers.data)
    
    #PUT
    elif request.method == 'PUT':
        serializer = GeustSerializer(geust, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status= status.HTTP_204_NO_CONTENT)
    #DELETE
    if request.method == 'DELETE':

        geust.delete()
        
        return Response(status= status.HTTP_204_NO_CONTENT)
 except Guest.DoesNotExist:
      return Response(status= status.HTTP_404_NOT_FOUND)