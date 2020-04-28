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
router.register('feedback', MailView)


urlpatterns = [
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('bookings/', BookingDetailsView.as_view({'get': 'get', 'post': 'post'}), name='bookroom',),          # Передает параметр 'id' комнаты в вьюшку
    path('front/', ObjectLimitPaginationView.as_view(), name='front'),
]


