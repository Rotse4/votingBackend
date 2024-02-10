from rest_framework import serializers
from django.contrib.auth.models import User
# from rest_framework.serializers import ModelSerializer
from account.models import Account



class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['regNo', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        """
        Check if password and password2 match.
        """
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords don't match")
        return data

    def save(self):
        """
        Create and save the user instance.
        """
        regNo = self.validated_data['regNo']
        username = self.validated_data['username']
        password = self.validated_data['password']
        
        # Create the user
        user = Account.objects.create_user(regNo=regNo, username=username, password=password)
        return user



