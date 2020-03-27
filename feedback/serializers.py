from .models import *
from rest_framework import serializers


class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = ('id', 'name', 'email', 'subject', 'message')
