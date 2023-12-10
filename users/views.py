import random

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from users.models import UserConfirm
from users.serializers import UserRegisterSerializers, UserConfirmSerializers, UserLoginSerializers


@api_view(['POST'])
def register_api_view(reguest):
    serializer = UserRegisterSerializers(data=reguest.data)
    serializer.is_valid(raise_exception=True)
    user = User.objects.create_user(**serializer.validated_data, is_active=False)

    confirm = UserConfirm.objects.create(user=user, code=random.randint(100000, 999999))
    return Response({'status': 'User registered', 'code': confirm.code, 'data': serializer.data},
                    status=HTTP_201_CREATED)

@api_view(['POST'])
def confirm_user_api_view(request):
    serializer = UserConfirmSerializers(data=request.data)
    serializer.is_valid(raise_exception=True)
    code =serializer.validated_data.get('code')
    confirm = get_object_or_404(UserConfirm, code=code)
    user = confirm.user
    user.is_active = True
    user.save()
    return Response({'status': 'User activated'}, status=status.HTTP_200_OK)
@api_view(['POST'])
def login_api_view(reguest):
    serializer = UserLoginSerializers(data=reguest.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(**serializer.validated_data)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        user.save()
        return Response({'token': token.key})
    return Response({'error': 'Invalid credentials'}, status=400)











