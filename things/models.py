from django.db.models import Model
from django.contrib.auth.models import AbstractUser

class Thing(Model):
    name = Model.TextField()
    description = Model.TextField()
    quantity = Model.IntegerField()
