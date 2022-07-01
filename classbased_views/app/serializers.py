
from app.models import Empmodel
from rest_framework import serializers

class Empserializers(serializers.ModelSerializer):
    class Meta:
        model = Empmodel
        fields = "__all__"