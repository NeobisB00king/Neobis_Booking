from django.db import models


class CategoryRoom(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория комнаты'
        verbose_name_plural = 'Категории комнат'

    def __str__(self):
        return self.name


class VolumeRoom(models.Model):
    volume_name = models.CharField(max_length=64, verbose_name='Вместительность комнаты')

    class Meta:
        verbose_name = 'Вместительность комнаты'
        verbose_name_plural = 'Вместительность комнат'

    def __str__(self):
        return self.volume_name


class Room(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название комнаты')
    price = models.IntegerField(default=0, blank=False, verbose_name='Цена')
    category = models.ForeignKey(CategoryRoom, default='', related_name='room_category', on_delete=models.CASCADE, verbose_name='Название категории')
    volume = models.ForeignKey(VolumeRoom, default='', related_name='room_volume', on_delete=models.CASCADE, verbose_name='Вместительность категории')
    images = models.ImageField(null=True, blank=True, verbose_name='Вместительность категории')

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

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

    date_from = models.DateField(verbose_name='Бронировать с')
    date_to = models.DateField(verbose_name='Бронировать до')
    comment = models.CharField(max_length=170, blank=True, verbose_name='Комментарий')
    Not_confirmed = 'NF'
    Confirmed = 'CO'
    Rejected = 'RE'
    book_status = models.CharField(
        max_length=13,
        choices=Book_Status_CHOICES,
        default=Not_confirmed,
        verbose_name='Статус брони'
    )
    book_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания брони')
    room = models.ForeignKey(Room, default='', on_delete=models.CASCADE, verbose_name='Комната')
    Paid = 'PA'
    Unpaid = 'UP'
    book_pay_status = models.CharField(
        max_length=6,
        choices=BOOK_PAY_CHOICES,
        default=Unpaid,
        verbose_name='Статус оплаты'
    )
    has_child = models.BooleanField(default=False, blank=True, verbose_name='Есть ли ребенок')
    clientName = models.CharField(max_length=64, verbose_name='Имя клиента')
    clientSurname = models.CharField(max_length=64, verbose_name='Фамилия клиента')
    clientEmail = models.EmailField(verbose_name='Email клиента')
    clientPhone = models.IntegerField(verbose_name='Номер телефона клиента')
    totalsum = models.IntegerField(verbose_name='Полная стоимость', default=0)
    room_category_stats = models.CharField(verbose_name='Категория комнаты для статистики', max_length=64,
                                           blank=True, default='')

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'

    def __str__(self):
        name = self.clientName + ' ' + self.clientSurname
        email = self.clientEmail
        booking = name + ', ' + email
        return booking

    def save(self, *args, **kwargs):
        self.totalsum += self.room.price
        # self.totalsum.save()
        self.room_category_stats += self.room.category.name
        super(Booking, self).save(*args, **kwargs)


class BookSummary(Booking):

    class Meta:
        proxy = True
        verbose_name = 'Статистика брони'
        verbose_name_plural = 'Статистка бронирования'


