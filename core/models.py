from django.db import models
# lets create a ListOfCaddies model
class ListOfCaddies(models.Model):
    name = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    def __str__(self):
        #when shown in admin youll see "name" then avalibiliy
        return f"{self.name} {self.available}"


class EndUsers(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.username  # return a string directly
    

    
class TeeTime(models.Model):
    time = models.CharField(max_length=100)
    user = models.ForeignKey(EndUsers, on_delete=models.CASCADE, related_name="tee_times")
    caddie = models.ForeignKey(ListOfCaddies, on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_tee_times")

    def __str__(self):
        return f"{self.time} - {self.user.username} - Caddie: {self.caddie.name if self.caddie else 'None'}"


  