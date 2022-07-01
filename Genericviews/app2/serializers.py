from dataclasses import fields
from app2.models import Workermodel
from rest_framework import serializers

class Workerserializer(serializers.ModelSerializer):
    class Meta:
        model = Workermodel
        fields = "__all__"
        