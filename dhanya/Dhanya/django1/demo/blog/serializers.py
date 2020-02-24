from rest_framework_mongoengine import serializers
from rest_framework import serializers
from .models import student_details
from rest_framework_mongoengine.serializers import DocumentSerializer


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model =student_details
        fields = '__all__'