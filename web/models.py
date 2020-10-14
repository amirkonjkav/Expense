from django.db import models
from django.contrib.auth.models import User


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=48)

    def __str__(self):
        return f"{self.user}-token"


class Expense(models.Model):
    text = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now=True)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text} - {self.amount}"


class Income(models.Model):
    text = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now=True)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text} - {self.amount}"
