from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from booking.rooms.email import send_reservation_email
from booking.rooms.models import Reservation


@receiver(pre_save, sender=Reservation)
def update_product_related(sender, **kwargs):
    instance = kwargs['instance']
    if instance.pk is None:
        return
    status = sender.objects.filter(
        pk=instance.pk).values('status')[0]['status']
    if instance.status == status:
        return

    send_reservation_email(instance, instance.user)
