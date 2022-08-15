import django_filters
from .models import *

class DoctorFilter(django_filters.FilterSet):
    class Meta:
        model = Doctors
        fields = ["name","specialization","hospital"]