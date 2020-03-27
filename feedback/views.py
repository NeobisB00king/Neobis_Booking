from django.shortcuts import render
from django.core.mail import send_mail
from django.core import mail
from django.conf import settings
from django.contrib import messages
# Create your views here.


from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Mail, AdminEmail
from .serializers import MailSerializer
from django.core.mail import EmailMessage


class MailView(viewsets.ModelViewSet):
    queryset = Mail.objects.all()
    serializer_class = MailSerializer

    def get(self, **kwargs):
        departments = self.queryset.all()
        serializer = self.serializer_class(departments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            connection = mail.get_connection()
            connection.open()
            name = serializer.data['name']
            email = serializer.data['email']
            subjectForm = serializer.data['subject']
            subject = 'Имя - "{}", Email - "{}", Тема - "{}"'.format(name, email, subjectForm)
            message = serializer.data['message']
            email_from = settings.EMAIL_HOST_USER
            field_name = 'email'
            obj = AdminEmail.objects.first()
            admin_email = getattr(obj, field_name)
            recipient_list = [admin_email, ]
            send_mail(subject, message, email_from, recipient_list,
                      connection=connection, fail_silently=False)
            print("Email (now) successfully sent!")
            connection.close()
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        messages.success(request, f'Письмо успешно отправлено!')
        return Response(serializer.data, status=status.HTTP_201_CREATED)

