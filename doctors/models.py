from django.db import models

# Create your models here.
class Doctors(models.Model):
    '''
    schema: "name","degree","specialization","hospital","experience","awards"
    '''
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    # hospital_id = models.IntegerField()
    hospital = models.CharField(max_length=255)
    experience = models.IntegerField()
    awards = models.IntegerField(blank=True)

    def __str__(self) -> str:
        return self.name + ' ' + self.specialization
