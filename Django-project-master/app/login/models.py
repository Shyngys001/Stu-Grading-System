from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Subject(models.Model):
    name = models.CharField(max_length=20)
    student = models.CharField(max_length=30)
    professor = models.CharField(max_length=30)
    grade = models.FloatField()
    date = models.DateField()
    observations = models.CharField(max_length=200)
