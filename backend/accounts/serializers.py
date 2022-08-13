from urllib import request
from pkg_resources import require
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
import email
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import CustomUser


import sys
from django.core import exceptions
import django.contrib.auth.password_validation as validators


from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated



class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class RegisterUserSerializer(serializers.ModelSerializer):
    '''
    This Class Serializer helps validate password, confirms password, email and 
    creates a user account if all condition is met and returns the user object
    created.
    '''
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    # this function is where all validation takes place
    # it is an extenstion of the default Django Model Validation
    def validate(self, data):
         
        # get the password and confirm_password from the data
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        username = data.get('username')

         
        errors = dict() 
        try:
            # validate the password and catch the exception
            validators.validate_password(password=password)

            # check if password if same with confirm_password
            if password != confirm_password:
                raise serializers.ValidationError({
                    'password': 'Password does not match'
                })
            if CustomUser.objects.filter(username= username).exists():
                raise serializers.ValidationError({
                    'username': 'User with this username already exist.'
                })

        # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)
         
        if errors:
            raise serializers.ValidationError(errors)
          
        return super(RegisterUserSerializer, self).validate(data)
        # return super().validate(attrs)

    def save(self):
        username=self.validated_data['username']
       
        try:
            user = CustomUser.objects.create_user(
                username = self.validated_data['username'],
                email = self.validated_data['email']
                # password=check if they match before seting the password
            )
            user.set_password(self.validated_data['password'])

            user.save()

            return user
        except Exception as e:
            raise serializers.ValidationError({
                "message": f'{e}'
            })

        

    class Meta:
        model = CustomUser
        fields = '__all__'


from rest_framework import serializers

# class LoginUserSerializer(serializers.Serializer):
#     model = CustomUser
#     token = serializers.CharField(max_length=50)

#     def validate(self, data):
         
#         # get the password and new_password from the data
#         token = data.get('token')

         
#         errors = dict() 
#         try:
#             # validate the password and catch the exception
#             if not CustomUser.auth_token.ob (key=token).exists():
#                 raise serializers.ValidationError({
#                     'token': 'Credentials provided is invalid!'
#                 })

#         # the exception raised here is different than serializers.ValidationError
#         except exceptions.ValidationError as e:
#             errors['password'] = list(e.messages)
         
#         if errors:
#             raise serializers.ValidationError(errors)
          
#         return super(ChangePasswordSerializer, self).validate(data)


class ChangePasswordSerializer(serializers.Serializer):
    model = CustomUser

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate(self, data):
         
        # get the password and new_password from the data
        password = data.get('new_password')

         
        errors = dict() 
        try:
            # validate the password and catch the exception
            validators.validate_password(password=password)

        # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)
         
        if errors:
            raise serializers.ValidationError(errors)
          
        return super(ChangePasswordSerializer, self).validate(data)


class UpdateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')
        
        
    def validate(self, data):
         
        # get the email and new_email from the data
        email = data.get('email')

         
        errors = dict() 
        try:
            # validate the password and catch the exception
            if CustomUser.objects.filter(email=email).exists():
                raise serializers.ValidationError(
                    {"email": "This email is already in use."})


        # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)
         
        if errors:
            raise serializers.ValidationError(errors)
          
        return super(UpdateUserSerializer, self).validate(data)


