from django.db import models

class empdata(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    mobile=models.BigIntegerField()
    company=models.CharField(max_length=50)
    salary=models.IntegerField()
    location=models.CharField(max_length=50)
