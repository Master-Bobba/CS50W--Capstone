from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    status = models.CharField(max_length=64, blank = False)

class Subject(models.Model):
    name = models.CharField(max_length=64, blank=False)
    teacher = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, related_name="classes")
    description = models.CharField(max_length=256, blank=True)
    core = models.BooleanField(default="True")
    students = models.ManyToManyField(User, blank=True)
    