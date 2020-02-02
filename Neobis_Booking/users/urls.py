from django.urls import path

from .views import RegistrationAPIView, LoginAPIView, login, UserLogin

app_name = 'users'

urlpatterns = [
    path('create/', RegistrationAPIView.as_view()),
    path('login/', UserLogin.as_view()),
]