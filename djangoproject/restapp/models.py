from django.db import models

# Create your models here.
class Customer(models.Model):
    custid = models.IntegerField(null=False, blank=False, primary_key=True)
    custname = models.CharField(max_length=100)
    custage = models.IntegerField()
    shopping = models.IntegerField()
