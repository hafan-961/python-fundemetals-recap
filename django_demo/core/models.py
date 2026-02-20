from django.db import models
#django database tool   
# Create your models here.

class Product(models.Model):
    #creating table named product
    name  = models.CharField(max_length = 50)
    price  = models.IntegerField()

#this creates datsbase table blueprint
#why we are doing this  ?
#ans)  because backend needs to store data permentaly 
#without model --> no database -> no real backend
