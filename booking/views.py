from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import status, viewsets
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
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


    # def get_serializer_class(self):
    #     """
    #     Determins which serializer to user `list` or `detail`
    #     """
    #     if self.action == 'retrieve':
    #         if hasattr(self, 'detail_serializer_class'):
    #             return self.detail_serializer_class
    #     return super().get_serializer_class()
    #
    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned queries by filtering against
    #     a `sport` and `name` query parameter in the URL.
    #     """
    #     queryset = Booking.objects.all()
    #     clientName = self.request.query_params.get('clientName', None)
    #     name = self.request.query_params.get('name', None)
    #     if clientName is not None:
    #         clientName = clientName.title()
    #         queryset = queryset.filter(client_name=clientName)
    #     if name is not None:
    #         queryset = queryset.filter(name=name)
    #     return queryset

