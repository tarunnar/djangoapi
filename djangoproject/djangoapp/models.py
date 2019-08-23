from django.db import models

# Create your models here.
class Employee(models.Model):
    empid = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=100)
    empage = models.IntegerField()
    empexp = models.IntegerField()