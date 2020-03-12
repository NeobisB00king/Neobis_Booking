from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.core import mail
from django.conf import settings


from .forms import IndexForm
from .models import AdminEmail

#Images upload imports
from django.forms import modelformset_factory
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .models import Images

# Create your views here.

class HomeView(TemplateView):
    name = 'feedback/feedback.html'

    def get(self, request):
        form = IndexForm()
        imageFormSet = modelformset_factory(Images, fields=('image', ))
        imageForm = imageFormSet()
        return render(request, self.name, {'form': form, 'imageForm': imageForm, })

    def post(self, request):
        #Email start -----------------------------------------
        form = IndexForm(request.POST)
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

        #Email end -----------------------------------------


class ImageUploadView(TemplateView):
    name = 'feedback/imageUpload.html'

    def get(self, request):
        imageFormSet = modelformset_factory(Images, fields=('image', ))
        form = imageFormSet()
        return render(request, self.name, {'form': form, })

    def post(self, request):
        #Load multiple images start -----------------------------------------
        if request.method == 'POST':
            imageFormSet = modelformset_factory(Images, fields=('image', ))
            form = imageFormSet(request.POST, request.FILES)

            if form.is_valid():
                form.save()

            return render(request, self.name, {'form': form, })
        #Load multiple images end -----------------------------------------
