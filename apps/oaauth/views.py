from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import LoginSerializer, UserSerializer
from datetime import datetime
from .authentications import generate_jwt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class LoginView(APIView):
    def post(self, request):
        # 验证数据是否可用
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data.get('user')
            user.last_login = datetime.now()
            user.save()
            token = generate_jwt(user)
            return Response({'token': token, 'user': UserSerializer(user).data})
        else:
            print(serializer.errors)
            return Response({'detail': "参数验证失败"}, status=status.HTTP_400_BAD_REQUEST)


#  鉴权基类 拦截器 重复的写法
# class AuthenticatedRequiredView:
#     permission_classes = [IsAuthenticated]


class ResetPassword(APIView):
    # class ResetPassword(APIView, AuthenticatedRequiredView):

    # 这里的request是drf封装的 rest_framework.request.Request
    # 鉴权写法
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        print(request  )
        print(request.user)
        return Response({"msg": "success"})
