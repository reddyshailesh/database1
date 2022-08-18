from django.db import models

# Create your models here.
class details(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    job=models.CharField(max_length=50)
    address=models.CharField(max_length=300)
