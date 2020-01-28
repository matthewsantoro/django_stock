from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Statuses(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Ranks(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
       return self.title

class Products(models.Model):
    title =models.CharField(max_length=200)
    count = models.IntegerField()
    desc = models.TextField()
    rank = models.ForeignKey(Ranks, on_delete=models.CASCADE)
    status = models.ForeignKey(Statuses, on_delete= models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now())
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title
  