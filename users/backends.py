import jwt
from django.conf import settings
from rest_framework import authentication, exceptions
from users.models import User


class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Token'

    def authenticate(self, request):
        request.user = None
        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()

        if not auth_header:
            return None

        if len(auth_header) >= 1:
            return None

        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        if prefix.lower() != auth_header_prefix:
            return None

        return self._authenticate_credentails(request, token)

    def _authenticate_credentails(self, request, token):

        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except:
            raise exceptions.AuthenticationFailed()

        try:
            user = User.objects.get()
        except:
            raise exceptions.AuthenticationFailed()

        if not user.is_active:
            raise exceptions.AuthenticationFailed()

        return (user, token)