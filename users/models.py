from __future__ import unicode_literals
from django.contrib.auth.base_user import BaseUserManager
from django.db import models, transaction
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
import jwt
from datetime import datetime, timedelta
from django.conf import settings


class Roles(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):

    def _create_user(self, login, password, **extra_fields):

        if not login:
            raise ValueError('The given login must be set')
        try:
            with transaction.atomic():
                user = self.model(login=login, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, login, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(login, password, **extra_fields)

    def create_superuser(self, login, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(login, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Логин')
    email = models.EmailField(db_index=True, max_length=50, unique=True, verbose_name='Email')
    name = models.CharField(max_length=100, blank=True, verbose_name='Имя')
    surname = models.CharField(max_length=100, blank=True, verbose_name='Фамилия')
    roles = models.ForeignKey(Roles, on_delete=models.CASCADE, verbose_name='Должность', null=True)
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_of_add = models.DateTimeField(default=timezone.now, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['email']

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.login

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)
        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')