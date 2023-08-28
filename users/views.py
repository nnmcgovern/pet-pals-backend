from rest_framework.decorators import api_view
from rest_framework.response import Response


from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


@api_view(['POST'])
def login(request):
    return Response({
        'message': '로그인 되었습니다.'
    })

@api_view(['POST'])
def sign_up(request):
    serializer = UserSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        user = serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({
            'token': token.key,"user":serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_token(request):
    return Response({
        'message': '로그인 되었습니다.'
    })


