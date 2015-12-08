from django.contrib.auth.models import User, Group
from app.models import *
from rest_framework import serializers

class UserCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustom
        fields = ('url','id', 'username', 'password')


class RiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Risk
        fields = ('url', 'name', 'category', 'description', 'type')
        
class RiskProjectSerializer(serializers.ModelSerializer):
    id_risk = RiskSerializer(many=False, read_only=True)
    
    class Meta:
        model = RiskProject
        fields = ('url', 'id_project', 'probability', 'id_risk',
        'impact', 'factors', 'reduction', 'supervision')

class ProjectSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(many=True, queryset=UserCustom.objects.all())
    risk_projects = RiskProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('url', 'title', 'id_category', 'description', 'start_date', 'end_date', 'members', 'id_owner', 'risk_projects')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'id', 'name')

