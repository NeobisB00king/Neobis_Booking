from django.db import models


# class Client(models.Model):
#     name = models.CharField(max_length=64)
#     surname = models.CharField(max_length=64)
#     email = models.CharField(max_length=100)
#     phone = models.IntegerField()

#     def __str__(self):
#         fullName = self.name + ' ' + self.surname
#         return fullName


class CategoryRoom(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class VolumeRoom(models.Model):
    volume_name = models.CharField(max_length=64)

    def __str__(self):
        return self.volume_name


class RoomImages(models.Model):
    image = models.ImageField(null=True)


class Room(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField(default=0, blank=False)
    capacity = models.IntegerField()
    category = models.ForeignKey(CategoryRoom, on_delete=models.CASCADE)
    volume = models.ForeignKey(VolumeRoom, on_delete=models.CASCADE)
    images = models.ForeignKey(RoomImages, null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    Book_Status_CHOICES = [
        ('Not_confirmed', 'Not_confirmed'),
        ('Confirmed', 'Confirmed'),
        ('Rejected', 'Rejected'),
    ]

    BOOK_PAY_CHOICES = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
    ]

    date_from = models.DateField()
    date_to = models.DateField()
    comment = models.CharField(max_length=170, blank=True)
    Not_confirmed = 'NF'
    Confirmed = 'CO'
    Rejected = 'RE'
    book_status = models.CharField(
        max_length=13,
        choices=Book_Status_CHOICES,
        default=Not_confirmed,
    )
    book_date = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    Paid = 'PA'
    Unpaid = 'UP'
    book_pay_status = models.CharField(
        max_length=6,
        choices=BOOK_PAY_CHOICES,
        default=Unpaid,
    )
    has_child = models.BooleanField(default=False, blank=True)
    clientName = models.CharField(max_length=64)
    clientSurname = models.CharField(max_length=64)
    clientEmail = models.EmailField()
    clientPhone = models.IntegerField()

    def __str__(self):
        # room = get_object_or_404(Room, pk=id)
        # room = Room.objects.filter(pk__in=self.room).
        name = self.clientName + ' ' + self.clientSurname
        email = self.clientEmail
        booking = name + ', ' + email
        return booking

