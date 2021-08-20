from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    mobile_no= models.IntegerField(max_length=10)
    designation=models.CharField(max_length=42)
    
    class Meta():
        db_table = "User"
        