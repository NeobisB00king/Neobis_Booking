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

    # totalsum = serializers.SerializerMethodField()
    #
    # def get_totalsum(self, request):
    #     sum = 0
    #     mto = Room.objects.filter(id=request.id)
    #     for s in mto:
    #         sum += s.price
    #     return sum
    # def get_totalsum(self, request):
    #     sum = 0
    #     mto = MealsToOrders.objects.filter(orderid=request.orderid)
    #     for s in mto:
    #         sum += s.count * s.mealsid.price
    #     return sum

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
            'clientPhone',
            'totalsum',
            'date_mass'
        )
        read_only_fields = ['totalsum', 'date_mass']
