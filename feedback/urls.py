from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('/feedback', MailView.as_view()),
    # path('img', ImageUploadView.as_view(), name='ImageUpload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)