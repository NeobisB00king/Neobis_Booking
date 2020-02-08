from django.db import models
# Create your models here.


class CategoryRoom(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название категории')
    volume = models.CharField(max_length=20, verbose_name='Вместительность')
    special = models.TextField(verbose_name='Дополнительная информация')
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Reservation(models.Model):
    PAID = 'P'
    UNPAID = 'UN'
    PAY_CHOICES = [(PAID, 'Paid'), (UNPAID, 'Unpaid')]
    name = models.CharField(max_length=10, verbose_name='Номер брони')
    client_name = models.CharField(max_length=50, verbose_name='Клиент')
    client_email = models.EmailField(max_length=100, verbose_name='Электронная почта клиента')
    time_from = models.DateField(verbose_name='Время заезда')
    time_to = models.DateField(verbose_name='Время выезда')
    sum_price = models.ImageField(max_length=100, verbose_name='Сумма')
    status_pay = models.CharField(max_length=10, choices=PAY_CHOICES, default=UNPAID)
    special_request = models.TextField(verbose_name='Возможные пожелания')

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=100, verbose_name='Номер комнаты')
    category = models.ForeignKey(CategoryRoom, on_delete=models.CASCADE, verbose_name='Тип номера', null=False)
    photos = models.ImageField(verbose_name='Фото')
    status = models.BooleanField(default=False, verbose_name='Статус')
    reservation = models.ForeignKey(Reservation, on_delete=models.SET_NULL, null=True, verbose_name='Бронь')

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

    def __str__(self):
        return self.name
