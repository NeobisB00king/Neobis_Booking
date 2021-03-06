import datetime, re, json, six

from django.core.mail import send_mail
from django.core import mail
from django.conf import settings

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
from .functions import test_for_date_validity, send_email_to_customer
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
        model = self.queryset.all()  # Booking model

        requestData = request.data
        roomName = requestData.__getitem__('room')
        dateFrom = requestData.__getitem__('date_from')
        dateTo = requestData.__getitem__('date_to')

        customerEmail = requestData.__getitem__('clientEmail')
        clientName = requestData.__getitem__('clientName')
        totalsum = request.POST.get('totalsum')


        dateFrom = datetime.datetime.strptime(dateFrom, "%Y-%m-%d").date()

        bookingsIdList = list(Booking.objects.filter(room__name=roomName).values('id'))
        idList = [None] * len(bookingsIdList)
        datesList = [None] * len(bookingsIdList)

        for _ in range(len(bookingsIdList)):
            temp = bookingsIdList[_]
            idList[_] = temp.get('id')

        for _ in range(len(bookingsIdList)):
            temp = list(Booking.objects.filter(id=idList[_]).values('date_to'))
            temp2 = temp[0]
            datesList[_] = temp2.get('date_to')

        serializer = self.serializer_class(data=request.data)
        if re.search("^Success", str(test_for_date_validity(dateFrom, datesList))) and serializer.is_valid(raise_exception=True):
            serializer.save()
            send_email_to_customer(clientName, roomName, dateFrom, dateTo, customerEmail, totalsum)
            return Response({
                'serializer': serializer.data, 
                "Success": "The booking has been created!",
                'status': status.HTTP_201_CREATED,
            }
            )
                
        elif re.search("^Taken", str(test_for_date_validity(dateFrom, datesList))):
            return Response({"Fail": "Room is already booked for this date!"}, status=status.HTTP_400_BAD_REQUEST)
        elif re.search("^Invalid", str(test_for_date_validity(dateFrom, datesList))):
            return Response({"Fail": "The date must be today or later!"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Fail": "Unexpected error has occured!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
