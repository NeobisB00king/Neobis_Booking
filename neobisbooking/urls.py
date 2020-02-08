"""neobisbooking URL Configuration

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
from django.urls import path
from users.views import *
from booking.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('users/', UserViewSet.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
    path('registration/', RegistrationAPIView.as_view()),
    path('login/', login),
    path('roles/', RolesViewSet.as_view(), name='roles', ),
    path('roles/<int:pk>/', RolesDetailView.as_view()), ]

urlpatterns += [
    path('category_rooms', CategoryRoomViewSet.as_view()),
    path('category_rooms/<int:pk>', CategoryRoomDetailView.as_view()),
    path('reservations', ReservationViewSet.as_view()),
    path('reservations/<int:pk>', ReservationDetailView.as_view()),
    path('rooms', RoomViewSet.as_view()),
    path('rooms/<int:pk>', RoomDetailView.as_view()),
]
