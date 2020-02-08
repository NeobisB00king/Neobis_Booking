from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.core import mail
from django.conf import settings


from feedback.models import AdminEmail
from .forms import *
# Create your views here.


class FeedbackView(TemplateView):
    name = 'feedback/feedback.html'

    def get(self, request, **kwargs):
        form = FeedbackForm()
        return render(request, self.name, {'form': form})

    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # form.save()

            connection = mail.get_connection()
            connection.open()

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subjectForm = form.cleaned_data['subject']

            subject = 'Имя - "{}", Email - "{}", Тема - "{}"'.format(name, email, subjectForm)
            message = form.cleaned_data['message']

            email_from = settings.EMAIL_HOST_USER

            field_name = 'email'
            obj = AdminEmail.objects.first()
            adminEmail = getattr(obj, field_name)

            recipient_list = [adminEmail, ]

            send_mail(subject, message, email_from, recipient_list,
                      connection=connection, fail_silently=False)

            print("Email (now) successfully sent!")

            connection.close()

        context = {
            'form': form,
        }

        return render(request, self.name, context)
