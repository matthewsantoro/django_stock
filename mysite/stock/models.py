from django.db import models
from django.conf import settings
from django.utils import timezone
from django.shortcuts import reverse

# Create your models here.


class Status(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'statuses'


class Rank(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)
    count = models.IntegerField()
    desc = models.TextField()
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now())
    end_date = models.DateTimeField(blank=True, null=True)

    def get_absulute_url(self):
        return reverse('product_detail_url', kwargs={'product_id' : self.id })

    def __str__(self):
        return self.title
