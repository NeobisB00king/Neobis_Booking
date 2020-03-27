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
        fields = ('id', 'name', 'price', 'capacity', 'category', 'volume', 'images')


    # def create(self, validated_data):
    #     volumes_data = validated_data.pop('volume')
    #     room = Room.objects.create(**validated_data)
    #     for volume_data in volumes_data:
    #         CategoryRoom.objects.create(room=room, **volume_data)
    #     return room

    # def create(self, validated_data):
    #     category_data = validated_data.pop('category')
    #     volume_data = validated_data.pop('volume')
    #     course = Room.objects.create(**validated_data)
    #     category_list = []
    #     volume_list = []
    #     print(category_data)
    #     print(volume_data)
    #     for category_details in category_data:
    #         category_list.append(models.Category.objects.create(
    #             course_id=course.id,
    #             **category_details
    #         ))
    #     for volume_details in volume_data:
    #         volume_list.append(models.Volume.objects.create(
    #             course_id=course.id,
    #             **volume_details
    #         ))
    #     course.save()
    #     return course


class BookingSerializer(serializers.ModelSerializer):
    room = RoomSerializer(many=True)

    class Meta:
        model = Booking
        fields = ('id', 'date_from', 'date_to', 'comment', 'book_status', 'room',
                  'book_pay_status', 'has_child', 'clientName', 'clientSurname',
                  'clientEmail', 'clientPhone')




