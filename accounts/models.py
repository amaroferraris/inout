from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class In(models.Model):
    user_in = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    amount = models.IntegerField(null=True)
    description = models.CharField(max_length=9, null=True)
    category = models.CharField(max_length=6, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"$ {self.amount}"


class Out(models.Model):
    user_out = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    amount = models.IntegerField(null=True)
    description = models.CharField(max_length=9, null=True)
    category = models.CharField(max_length=6, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"${self.amount}"    

# class In(models.Model):
    # user_in = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    # amount = models.IntegerField(null=True)
    # description = models.CharField(max_length=15, null=True)
    # category = models.CharField(max_length=15, null=True)
    # date_created = models.DateTimeField(auto_now_add=True, null=True)
# 
    # def __str__(self):
        # formatted_date = self.date_created.strftime('%d-%m-%y')
        # return f"${self.amount} | {self.user_in} | {formatted_date}"
# 
# class Out(models.Model):
    # user_out = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    # amount = models.IntegerField(null=True)
    # description = models.CharField(max_length=15, null=True)
    # category = models.CharField(max_length=15, null=True)
    # date_created = models.DateTimeField(auto_now_add=True, null=True)
# 
    # def __str__(self):
        # formatted_date = self.date_created.strftime('%d-%m-%y')
        # return f"${self.amount} | {self.user_out} | {formatted_date}"
