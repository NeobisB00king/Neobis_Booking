import datetime

from .models import *
from rest_framework import serializers


class CategoryRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryRoom
        fields = ('id', 'name')


class VolumeRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolumeRoom
        fields = ('id', 'volume_name')


class RoomSerializer(serializers.ModelSerializer):
    category = CategoryRoomSerializer()
    volume = VolumeRoomSerializer()
    # images = RoomImagesSerializer()

    class Meta:
        model = Room
        fields = (
        'id', 
        'name', 
        'price',
        'category', 
        'volume', 
        'images'
        )


class BookingSerializer(serializers.ModelSerializer):
    room = serializers.SlugRelatedField(
        queryset=Room.objects.all(), slug_field='name')

    class Meta:
        model = Booking
        fields = (
        'id', 
        'date_from', 
        'date_to', 
        'comment', 
        'room', 
        'has_child', 
        'clientName', 
        'clientSurname', 
        'clientEmail', 
        'clientPhone'
        )





