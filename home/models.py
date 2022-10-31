from django.db import models

# Create your models here.

class Student(models.Model):
    fullname=models.CharField(max_length=100)
    stud_code=models.CharField(max_length=6)
    mobile=models.CharField(max_length=15)
    address=models.TextField()

    def __str__(self):
        return self.fullname