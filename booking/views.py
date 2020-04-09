import datetime

from django.http import HttpResponse, QueryDict
from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from .models import *
from .serializers import *
# Create your views here.


# class RoomViewSet(generics.ListCreateAPIView):
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


# class RoomDetailsView(generics.RetrieveAPIView):
class RoomDetailsView(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get(self, request, **kwargs):
        model = self.queryset.all()
        serializer = self.serializer_class(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookingDetailsView(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    roomqueryset = Room.objects.all()
    
    serializer_class = BookingSerializer
    serializer_room = RoomSerializer

    def get(self, request, *args, **kwargs):
        model = self.queryset.all()
        serializer = self.serializer_class(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        model = self.queryset.all() #Booking model
        roomModel = self.roomqueryset.filter(pk=kwargs['id']) #Room model

        #Edit request data to add room data to request
        
        roomSerializer = self.serializer_room(Room.objects.get(pk=self.kwargs['id'])) #Find resired room by id
        roomData = roomSerializer.data #Put room data inro a variable

        bookData = request.data #Take request data and put it into a varible to modify
        _mutable = bookData._mutable
        bookData._mutable = True
        bookData['room'] = roomData
        rightOrderList = ['csrfmiddlewaretoken', 'date_from', 'date_to', 'comment', 'book_status',
                      'room', 'book_pay_status', 'clientName', 'clientSurname', 'clientEmail', 'clientPhone']
        orderedBookData = dict()
        orderedBookData = {k: bookData[k] for k in rightOrderList}
        queryOrderedBookData = QueryDict('', mutable=True)
        queryOrderedBookData.update(orderedBookData)
        
        bookData = queryOrderedBookData
        bookData._mutable = True
        print(bookData)

        #End of editing request data

        serializer = self.serializer_class(data=bookData)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        else:
            print('Serializer not saved, there is something wrong')
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
