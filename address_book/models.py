from django.db import models
from users.models import CustomUser


class AddressBook(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    organization = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    house_num = models.IntegerField()
