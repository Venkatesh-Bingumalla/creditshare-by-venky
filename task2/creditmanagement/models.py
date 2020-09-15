from django.db import models

# Create your models here.
class AddUser(models.Model):
    Name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    credit =models.IntegerField()
class TransferMoney(models.Model):
    SenderName = models.CharField(max_length=100)
    ReName = models.CharField(max_length=100)
    Credits = models.IntegerField()