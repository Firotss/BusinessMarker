from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    pasword = models.CharField(max_length=200)
    reg_date = models.DateTimeField()
    account_type = models.CharField(max_length=200)

class Ref_Links(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    code = models.CharField(max_length=200)

