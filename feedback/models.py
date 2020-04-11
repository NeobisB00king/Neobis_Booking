from django.db import models
# Create your models here.


class AdminEmail(models.Model):
    email = models.EmailField()

    class Meta:
        verbose_name = 'Email админа'
        verbose_name_plural = "Email'ы админа"

    def __str__(self):
        return self.email


class Mail(models.Model):
    name = models.CharField(max_length=16)
    email = models.CharField(max_length=50, null=False)
    subject = models.CharField(max_length=30)
    message = models.TextField(blank=False, null=False)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    class Meta:
        db_table = 'Mail'


class Images(models.Model):
    image = models.ImageField(upload_to='imageUpload/pics')

    class Meta:
        verbose_name_plural = "Images"

