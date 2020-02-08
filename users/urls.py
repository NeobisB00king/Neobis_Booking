from django.urls import path

from users.views import RegistrationAPIView, UserLogin

app_name = 'users'

urlpatterns = [
    path('create/', RegistrationAPIView.as_view()),
    path('login/', UserLogin.as_view()),
]