from .serializers import UserRegistrationSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response ({'msg': 'Registration success'}, status=status.HTTP_200_OK)
        return Response (serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)



