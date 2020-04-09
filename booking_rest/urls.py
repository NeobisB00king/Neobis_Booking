"""booking_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from feedback.views import *
from booking.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('rooms', RoomViewSet)
router.register('bookings', BookingDetailsView)
router.register('feedback', MailView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('jet_api/', include('jet_django.urls')),
    path('', include(router.urls)),
    path('rooms/<int:id>/book/', BookingDetailsView.as_view({'get': 'get', 'post': 'post'}), name='bookroom',),          # Передает параметр 'id' комнаты в вьюшку
    # path('feedback/', MailView.as_view({'get': 'list'}), name='feedback'),
    # path('rooms/', RoomViewSet.as_view(), name='rooms',),
    # path('room/<int:pk>', RoomDetailsView.as_view(), name='room',),                 # Нужно указать id, т.е урл выглядит так: http://localhost:8000/room/1
    # path('room/', RoomDetailsView.as_view(), name='room',),                         # Не нужно указывать id,  т.е урл выглядит так: http://localhost:8000/room/
    # path('booking/<int:pk>', BookingDetailsView.as_view(), name='booking_detail '), # Нужно указать id, т.е урл выглядит так: http://localhost:8000/booking/1
    # path('booking/', BookingDetailsView.as_view(), name='booking_detail '),         # Не нужно указывать id,  т.е урл выглядит так: http://localhost:8000/booking/

]


