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


class RoomImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImages
        fields = ('id', 'image')


class RoomSerializer(serializers.ModelSerializer):
    category = CategoryRoomSerializer(many=True)
    volume = VolumeRoomSerializer(many=True)
    images = RoomImagesSerializer(many=True)

    class Meta:
        model = Room
        fields = ('id', 'name', 'price', 'capacity',
                  'category', 'volume', 'images',)


class BookingSerializer(serializers.ModelSerializer):
    room = RoomSerializer(many=True)

    class Meta:
        model = Booking
        fields = ('id', 'date_from', 'date_to', 'comment', 'book_status', 'room',
                  'book_pay_status', 'has_child', 'clientName', 'clientSurname',
                  'clientEmail', 'clientPhone')
    def create(self, validated_data):
        room = Room.objects.get(pk=validated_data.pop('name'))
        booking = Booking.objects.create(**validated_data, room=room)
        return booking




