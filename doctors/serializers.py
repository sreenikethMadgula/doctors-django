from rest_framework import serializers
from .models import Doctors
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = ['id', 'name', 'degree', 'specialization', 'hospital', 'experience', 'awards']