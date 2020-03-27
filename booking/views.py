from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import status, viewsets, filters
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
# Create your views here.


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetailsView(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['category', 'volume']

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
    serializer_class = BookingSerializer

    def get(self, request, **kwargs):
        model = self.queryset.all()
        serializer = self.serializer_class(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)