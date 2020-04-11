from django.apps import AppConfig


class BookingConfig(AppConfig):
    name = 'booking'

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'
