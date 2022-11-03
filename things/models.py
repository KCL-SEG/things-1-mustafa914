from enum import unique
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Thing(models.Model):
    name = models.CharField(max_length=30, blank = False, unique = True)
    description = models.CharField(unique = False, blank = False, max_length = 120)
    quantity = models.IntegerField(unique = False, validators = [MinValueValidator(0), MaxValueValidator(100)])

