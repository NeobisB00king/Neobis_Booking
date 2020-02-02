from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serializers import *
from users.models import *
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate


class RegistrationAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request, **kwargs):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, **kwargs):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


# class UserLogin(ObtainAuthToken):
#     permission_classes = (AllowAny,)
#     # serializer_class = LoginSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         # token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'user_id': user.pk,
#         })


class UserLogin(ObtainAuthToken):
    permission_classes = (AllowAny,)
    serializers_class = LoginSerializer

    def get(self, request, format=None):
        allquery = User.objects.all()
        serializer = LoginSerializer(allquery, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
                'user_id': user.pk,
                'token': token.key,
            })

    # def get(self, request, *args, **kwargs):
    #     user = self.queryset.get_or_create(login=login)
    #     serializers = self.serializer_class(user, many=True, data=request.data, context={'request': request})
    #     return Response(serializers.data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


# class RolesViewSet(generics.ListCreateAPIView):
#     queryset = Roles.objects.all()
#     serializer_class = RolesSerializer


# class RolesDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Roles.objects.all()
#     serializer_class = RolesSerializer


class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
# Create your views here.
