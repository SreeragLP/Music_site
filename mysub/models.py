from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    accnumber=models.IntegerField()
    acctype=models.CharField(max_length=200)
    balance = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return str(self.accnumber)


class Subscribe(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.IntegerField()

    def __str__(self):
        return str(self.user)
