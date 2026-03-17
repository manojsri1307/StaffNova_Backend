from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Employee


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','password','email'] 
        extra_kwargs = {'password':{'write_only':True}}

    def create(self,validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = ['user']