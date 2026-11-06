from .serializers import UserRegistrationSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response


class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        return Response ({'msg': 'Registration success'})



