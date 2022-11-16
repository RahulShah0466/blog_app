from django.db import models

class BankDetail(models.Model):
    bank=models.CharField(max_length=80)
    accountno=models.IntegerField(max_length=100)
    accountname=models.CharField(max_length=50)



