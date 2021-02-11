from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length = 20)
    subject = models.CharField(max_length = 30)
    decription = models.TextField()

    def __str__(self):
        return self.name