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
    

    
# class TeeTimes(models.Model):
#     tee_time = models.CharField(max_length=100)
#     user = EndUsers.objects.create(username="john_doe", email="john@example.com")
#     caddie = ListOfCaddies.objects.create(name="Caddie Mike")
#     def __str__(self):
#         return f"TeeTime: {self.tee_time} - User: {self.user.username}"



  