from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Department, Profile, Indicator

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name', 'description')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'department')

class IndicatorSerializer(serializers.ModelSerializer):
    department_id = serializers.IntegerField(write_only=True)
    department = DepartmentSerializer(read_only=True)  # только для чтения

    class Meta:
        model = Indicator
        fields = ['id', 'name', 'description', 'department', 'department_id', 'fact_value', 'plan_value', 'month']