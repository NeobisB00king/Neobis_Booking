from django.db import models

from django.conf import settings

# Create your models here.
class AdminEmail(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

class Images(models.Model):
    image = models.ImageField(upload_to='imageUpload/pics')

    class Meta:
        verbose_name_plural = "Images"

