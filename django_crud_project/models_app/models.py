from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=400)
    
    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=400)
    
    def __str__(self):
        return self.name


class CertificateType(models.Model):
    name = models.CharField(max_length=400)
    
    def __str__(self):
        return self.name
    
class Grade(models.Model):
    type = models.CharField(max_length=400)
    
    def __str__(self):
        return self.type

class Department(models.Model):
    name = models.CharField(max_length=400)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    fullname = models.CharField(max_length=100)
    year_of_graduation = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    grade =  models.ForeignKey(Grade, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    certificate_type = models.ForeignKey(CertificateType, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.fullname
