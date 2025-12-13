from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Department, Profile

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name', 'description')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True)
    department = DepartmentSerializer(many=True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'department')

