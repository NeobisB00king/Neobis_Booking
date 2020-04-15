from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.translation import ugettext_lazy as _
import uuid

# auth_user = settings.AUTH_USER_MODEL if getattr(
#     settings, "AUTH_USER_MODEL") else User


class UserComments(models.Model):
    text = models.TextField()


class CategoryRoom(models.Model):
    category = models.CharField(max_length=20)


class User(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField(unique=True)


class VolumeCategoryRoom(models.Model):
    volume = models.CharField(max_length=20)


# Images model need to import with pillow model for dowmnload images


class ReservationStatuses(models.Model):
    status = models.CharField(max_length=20)


class PayStatuses(models.Model):
    pay_status = models.CharField(max_length=20)


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reserved_start_date = models.DateTimeField(default=timezone.now)
    reserved_end_date = models.DateTimeField()
    num_of_people = models.IntegerField(default=1)
#   room = models.ForeignKey(Room, on_delete=models.CASCADE)
    status = models.ForeignKey(ReservationStatuses, on_delete=models.SET_NULL)
    updated_datetime = models.DateTimeField(auto_now=True)
    user_comments = models.ForeignKey(UserComments, on_delete=models.SET_NULL)
    pay_status = models.ForeignKey(PayStatuses, on_delete=models.SET_NULL())

    # def __str__(self):
    #     return "%s  %s  (%s to %s)" % (self.user.get_full_name(),
    #                                    self.get_status_display(),
    #                                    self.reserved_start_date.strftime(
    #         "%Y/%m/%d %H:%S"),
    #         self.reserved_end_date.strftime(
    #         "%Y/%m/%d %H:%S"),
    #     )


class Room(models.Model):

    reservation = models.ForeignKey(Reservation,  on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryRoom, on_delete=models.CASCADE)
    volume = models.ForeignKey(VolumeCategoryRoom, on_delete=models.CASCADE)
    is_booked = models.BooleanField(default=False)
    booked_from = models.ForeignKey(Reservation, on_delete=models.SET_NULL)
#    booked_to = models.() need  to ralize that with forms
    is_taken = models.BooleanField(default=False)
#    images import with pillow images model

    @property
    def available_taken(self):
        return getattr(self.is_taken, self.is_booked)

    # @property
    # def amount_without_this_product(self):
    #     amount_now = self.available_amount
    #     return amount_now - self.amount
    #
    # def __str__(self):
    #     return "%.2f ) %s" % (self.amount, self.content_object)


class ReservationToken(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    base_url = models.URLField(default="http://localhost:8000")
