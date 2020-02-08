from rest_framework import serializers
from .models import *


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('name', 'category', 'photos', 'status', 'reservation')


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('name', 'client_name', 'client_email', 'status_pay', 'time_from', 'time_to',
                  'sum_price', 'special_request')  # добавить потом клиента


class CategoryRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryRoom
        fields = ('name', 'volume', 'special', 'price')