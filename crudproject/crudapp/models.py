from django.db import models

# Create your models here.
class studentdata(models.Model):
    sname=models.CharField(max_length=20)
    sage=models.IntegerField()
    saddr=models.CharField(max_length=20)
    m1=models.IntegerField()
    m2=models.IntegerField()
