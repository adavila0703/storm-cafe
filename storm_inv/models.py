from django.db import models

class Snack(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    amount = models.FloatField(null=True, default=0)
    price = models.FloatField(null=True, default=0)

    def __str__(self):
        return f"{self.name}"

class Person(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    lname = models.CharField(max_length=100, default="")
    money = models.FloatField(null=True, default=0)
    movement = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.lname}, {self.name}"

    def __int__(self):
        return self.money
