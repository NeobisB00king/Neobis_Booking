from rest_framework import generics
from booking.serializers import *
from booking.models import *


class CategoryRoomViewSet(generics.ListCreateAPIView):
    queryset = CategoryRoom.objects.all()
    serializer_class = CategoryRoomSerializer


class CategoryRoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryRoom.objects.all()
    serializer_class = CategoryRoomSerializer


class ReservationViewSet(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class RoomViewSet(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
