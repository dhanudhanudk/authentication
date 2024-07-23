from django.db import models
from django.contrib.auth.models import User

class SampleData(models.Model):
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)

    class Meta:
        db_table="sampledata"

class APIKey(models.Model):
    key=models.CharField(max_length=100,unique=True)
    create=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table="APIkey"