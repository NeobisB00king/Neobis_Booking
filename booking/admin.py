from django.contrib import admin

from .models import *

class BookingAdmin(admin.ModelAdmin):
    list_display = ('clientEmail', 'room', 'date_from',
                    'date_to', 'book_status')
    list_filter = ('book_status', 'room', 'book_date')

# admin.site.register(Client)
admin.site.register(Room)
admin.site.register(Booking, BookingAdmin)
admin.site.register(CategoryRoom)
admin.site.register(VolumeRoom)
# admin.site.register(RoomImages)

