from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()


class CategoryRoom(models.Model):
    name = models.CharField(max_length=64)


class VolumeRoom(models.Model):
    volume_name = models.CharField(max_length=64)


class RoomImages(models.Model):
    image = models.ImageField()


class Room(models.Model):
    name = models.CharField(max_length=64)
    capacity = models.IntegerField()
    category = models.OneToOneField(CategoryRoom, on_delete=models.CASCADE)
    volume = models.OneToOneField(VolumeRoom, on_delete=models.CASCADE)
    images = models.ForeignKey(RoomImages, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Booking(models.Model):
    date_from = models.DateField()
    date_to = models.DateField()
    comment = models.CharField(max_length=170)
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    Not_confirmed = 'NF'
    Confirmed = 'CO'
    Rejected = 'RE'
    Book_Status_CHOICES = [
        (Not_confirmed, 'Not_confirmed'),
        (Confirmed, 'Confirmed'),
        (Rejected, 'Rejected'),
    ]
    book_status = models.CharField(
        max_length=2,
        choices=Book_Status_CHOICES,
        default=Not_confirmed,
    )
    book_date = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    Paid = 'PA'
    Unpaid = 'UP'
    BOOK_PAY_CHOICES = [
        (Paid, 'Paid'),
        (Unpaid, 'Unpaid'),
    ]
    book_pay_status = models.CharField(
        max_length=2,
        choices=BOOK_PAY_CHOICES,
        default=Unpaid,
    )
    price = models.IntegerField()
    has_child = models.BooleanField(default=False)

    class Meta:
        unique_together = [['date', 'room']]