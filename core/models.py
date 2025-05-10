from django.db import models
# Create your models here.
# lets create a ListOfCaddies model
class ListOfCaddies(models.Model):
    name = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    def __str__(self):
        #when shown in admin youll see "name" then avalibiliy
        return f"{self.name} {self.available}"





  