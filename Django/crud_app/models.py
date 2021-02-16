from django.db import models

# Create your models here.
class EmployeeModel((models.Model)):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    contact = models.IntegerField(max_length=10)
    
    class Meta:
        db_table = "employee"