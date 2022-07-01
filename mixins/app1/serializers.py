from app1.models import Stumodel
from rest_framework import serializers

class Stuserializer(serializers.ModelSerializer):
    class Meta:
        model = Stumodel
        fields = "__all__"