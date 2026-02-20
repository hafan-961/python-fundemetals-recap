from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=1000)
    age = models.IntegerField()
    email = models.CharField(unique=True)
    def __str__(self):
        return self.name
