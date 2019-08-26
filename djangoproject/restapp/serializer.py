from rest_framework import serializers
from .models import Customer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import exceptions

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    def validate(self, data):
        username = data.get("username","")
        password  = data.get("password","")
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"]=user
                else:
                    msg = "Account is not Active"
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with given credentials"
                raise exceptions.ValidationError(msg)
        else:
            msg = "Specify username and password for login"
            raise exceptions.ValidationError(msg)
        return data
