from django.contrib.auth.models import User, Group
from app.models import *
from rest_framework import serializers

class UserCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustom
        fields = ('url', 'username', 'password')


class RiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Risk
        fields = ('url', 'name', 'category', 'description', 'type')

class ProjectSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    risks = RiskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('url', 'title', 'members', 'risks')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'name')

class RiskProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskProject
        fields = ('url', 'id_project', 'probability', 'id_risk',
        'impact', 'factors', 'reduction', 'supervision')
