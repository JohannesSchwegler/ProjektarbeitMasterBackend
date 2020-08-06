from django.db import models

# Create your models here.




class Card(models.Model):
    name= models.CharField(max_length=50)
    content= models.CharField(max_length=250)

    #display name in admin view
    def __str__(self):
        return self.name

