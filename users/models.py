from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.

class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=40,unique=True)
    password=models.CharField(max_length=12,null=False)
    role=models.CharField(choices=(('User','user'),('Reseller','reseller')),default='User')
    address=models.CharField(max_length=100,null=False)
    mobile_number=models.IntegerField()



