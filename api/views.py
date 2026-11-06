from .serializers import UserRegistrationSerializer, UserLoginSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate


class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response ({'msg': 'Registration success'}, status=status.HTTP_200_OK)
        return Response (serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)




class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                return Response({'msg': 'login success'}, status=status.HTTP_200_OK)
            else:
                return Response ({'error': {'non_field_errors': ['Email or password is not valid']}}, status=status.HTTP_404_NOT_FOUND)













