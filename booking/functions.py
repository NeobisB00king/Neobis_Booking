import datetime

from .models import *


start_date = datetime.date(2020, 3, 21)  # взять дату начала брони
end_date = datetime.date(2020, 3, 24)  # взять дату конца брони
day_delta = datetime.timedelta(days=1)  # с этим оно работает.
d = [start_date + i * day_delta for i in range((end_date - start_date).days)]  # создать доп параметр класса,
# чтобы было проще, который высчитывается вот так, не знаю почему это работает, но работает

for i in range((end_date - start_date).days):
    a = []
    c = start_date + i*day_delta
    print(c)
    a.append(i)


def get_date_array(start_date, end_date):
    day_delta = datetime.timedelta(days=1)
    d = [start_date + i * day_delta for i in range((end_date - start_date).days)]  # аналогичная функция, хз зачем,
    # может тебе будет удобнее.
    return d


print(get_date_array(start_date, end_date))


# написал я некое подобие, которое скорее всего работать не будет, потому что надо нормально тестить на проекте
# Думаю, когда бронь будет готова надо будет на ней вместе проетстить эту отправку,
# потому что я не совсем понял как это работает
def send_reservation():
    from django.core.mail import send_mail
    from django.core import mail
    connection = mail.get_connection()
    connection.open()
    email_from = settings.EMAIL_HOST_USER
    field_name = 'email'
    obj = Bookimg.objects.first()
    client_email = getattr(obj, field_name)
    subject = 'Напоминание о вашей брони'
    # form найти форму брони и взять оттуда данные
    message = form.cleaned_data['__all__']
    send_mail(subject, message, email_from, client_email,
              connection=connection, fail_silently=False)
    connection.close()