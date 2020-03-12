from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('feedback', HomeView.as_view(), name='Feedback'),
    path('img', ImageUploadView.as_view(), name='ImageUpload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
