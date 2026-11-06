from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ["email", "name", "password", "password2", "tc"]

        extra_kwargs={'write_only': True}



    