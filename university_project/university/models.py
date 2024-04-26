from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    course = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name
