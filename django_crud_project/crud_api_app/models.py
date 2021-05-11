from django.db import models
from django.utils.timezone import now

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length = 400)
    address = models.CharField(max_length = 400)
    postal_code = models.IntegerField()
    
    def __str__(self):
        return self.name
    


class Student(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    date_of_resumption = models.DateTimeField(default=now, editable=False)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    

    
                                 
    
    