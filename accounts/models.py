from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class InOutUser(models.Model):

#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=15, null=True)
#     email = models.CharField(max_length=20, null=True)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)

#     def __str__(self):
#         return str(self.user)




class In(models.Model):
    user_in = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    amount = models.IntegerField(null=True)
    description = models.CharField(max_length=15, null=True)
    category = models.CharField(max_length=15, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user_in)


class Out(models.Model):
    user_out = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    amount = models.IntegerField(null=True)
    description = models.CharField(max_length=15, null=True)
    category = models.CharField(max_length=15, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user_out)