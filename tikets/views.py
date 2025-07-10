from django.http import Http404
from django.shortcuts import render
from .models import Guest, Movie, Reservation
from rest_framework.decorators import api_view
from .serializers import GeustSerializer,MovieSerializer,ReservationSerializer
from tikets import serializers
from rest_framework.response import Response
from rest_framework import status , filters
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework import generics, mixins, viewsets


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
 

 


#CBV Class based views
#4.1 LIST and Create = GET and POST
class CBV_LIST(APIView):
    def get(self, request):
        guests = Guest.objects.all()
        serializer = GeustSerializer(guests, many= True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = GeustSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status= status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status= status.HTTP_400_BAD_REQUEST
        )
    

#4.2 get put and delet
class CBV_pk(APIView):

    def get_object(self, pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            raise Http404
    def get(self , request, pk):
        guest = self.get_object(pk)
        serializer = GeustSerializer(guest)
        return Response(serializer.data)
    

    def put(self, request, pk):
        guest = self.get_object(pk)
        serializer = GeustSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    

#5 mixins 
class mixins_list(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GeustSerializer

    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)
#5.1 mixins get put delet
class mixins_pk(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
     queryset = Guest.objects.all()
     serializer_class = GeustSerializer

     def get(self, request, pk):
        return self.retrieve(request)
     def put(self, request, pk):
        return self.update(request) 
     def delete(self, request, pk):
        return self.destroy(request)
     
#6 generics
class generic_list(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GeustSerializer

class generic_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GeustSerializer

#viewset
class viewset_guest(viewsets.ModelViewSet):

    queryset = Guest.objects.all()
    serializer_class = GeustSerializer

@api_view(['GET', 'POST'])
def FBV_ListMO(request):
    
    #GET
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializers = MovieSerializer(movie)
        return Response(serializers.data)
    
    #POST
    elif request.method == 'POST':
        serializer = MovieSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT', 'DELETE'])
def FBmov_pk(request, pk):
 try:
    mov = Movie.objects.get(pk=pk)
 
    #GET
    if request.method == 'GET':
        serializers = MovieSerializer(mov)
        return Response(serializers.data)
    
    #PUT
    elif request.method == 'PUT':
        serializer = MovieSerializer(mov, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status= status.HTTP_204_NO_CONTENT)
    #DELETE
    if request.method == 'DELETE':

        mov.delete()
        
        return Response(status= status.HTTP_204_NO_CONTENT)
 except Guest.DoesNotExist:
      return Response(status= status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def FBV_Listre(request):
    
    #GET
    if request.method == 'GET':
        res = Reservation.objects.all()
        serializers = ReservationSerializer(res, many=True)
        return Response(serializers.data)
    
    #POST
    elif request.method == 'POST':
        serializer = ReservationSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
def FBre_pk(request, pk):
 
 try:
    res = Reservation.objects.get(pk=pk)
 
    #GET
    if request.method == 'GET':
        serializers = ReservationSerializer(res)
        return Response(serializers.data)
    
    #PUT
    elif request.method == 'PUT':
        serializer = ReservationSerializer(res, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status= status.HTTP_204_NO_CONTENT)
    #DELETE
    if request.method == 'DELETE':

        res.delete()
        
        return Response(status= status.HTTP_204_NO_CONTENT)
 except Guest.DoesNotExist:
      return Response(status= status.HTTP_404_NOT_FOUND)
 




#7.1 LIST and Create  de movie= GET and POST
class mov_clas(APIView):
    def get(self, request):
        mov = Movie.objects.all()
        serializer = MovieSerializer(mov, many= True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status= status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status= status.HTTP_400_BAD_REQUEST
        )
    
#7.2 get put and delet de movie
class movcl_pk(APIView):

    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404
    def get(self , request, pk):
        mov = self.get_object(pk)
        serializer = MovieSerializer(mov)
        return Response(serializer.data)
    

    def put(self, request, pk):
        mov = self.get_object(pk)
        serializer = MovieSerializer(mov, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        mov = self.get_object(pk)
        mov.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    
class res(APIView):
    def get(self, request):
       res = Reservation.objects.all()
       serializer = ReservationSerializer(res, many = True )
       return Response(serializer.data)
    

    def post(self, request):
        serializer = ReservationSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status= status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status= status.HTTP_400_BAD_REQUEST
        )
    
#7.2 get put and delet de reservation
class rescl_pk(APIView):

    def get_object(self, pk):
        try:
            return Reservation.objects.get(pk=pk)
        except Reservation.DoesNotExist:
            raise Http404
    def get(self , request, pk):
        res = self.get_object(pk)
        serializer = ReservationSerializer(res)
        return Response(serializer.data)
    

    def put(self, request, pk):
        res = self.get_object(pk)
        serializer = ReservationSerializer(res, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        res = self.get_object(pk)
        res.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


#visets movi et reservation
class viewset_movie(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_bakend = [filters.SearchFilter]
    search_fields = ['movie']

class viewset_reservation(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

@api_view(['GET'])
def find_movie(request):
    movies = Movie.objects.filter(
        hall = request.data['hall'],
        movie = request.data['movie'],
    )
    serializer = MovieSerializer(movies, many= True)
    return Response(serializer.data)
