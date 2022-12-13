from django.db import models

# Create your models here.

class In(models.Model):
    amount = models.IntegerField(null=True)
    description = models.CharField(max_length=15, null=True)
    category = models.CharField(max_length=15, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return (self.description)


class Out(models.Model):
    amount = models.IntegerField(null=True)
    description = models.CharField(max_length=15, null=True)
    category = models.CharField(max_length=15, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return (self.description)