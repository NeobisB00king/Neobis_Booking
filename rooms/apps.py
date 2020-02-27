from django.apps import AppConfig


class RoomsConfig(AppConfig):
    name = 'rooms'

    def ready(self):
        import booking.rooms.signals
        AppConfig.ready(self)