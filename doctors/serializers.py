from rest_framework import serializers
from .models import Doctors

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = ["name","specialization","hospital"]

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = "__all__"