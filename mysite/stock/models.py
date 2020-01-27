from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Products(models.Model):
    title =models.CharField(max_length=200)
    count = models.IntegerField()
    desc = models.TextField()
    rank = models.ForeignKey(Ranks, on_delete=models.CASCADE)
    status = models.ForeignKey(Statuses, on_delete= models.CASCADE)


class Statuses(models.model):
    title = models.CharField(max_length=100)

class Ranks(models.Model):
    title = models.CharField(max_length=100)
    

