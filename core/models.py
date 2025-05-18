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
    


class Caddie(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name  # return a string directly
    
class Field(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name  # return a string directly

class Assignment(models.Model):
    #links one caddie to one feild
    caddie = models.OneToOneField(
        Caddie, on_delete=models.CASCADE,
    )
    field = models.OneToOneField(
        Field,
        on_delete=models.CASCADE,
    )
    #save the timestamp
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # For admin panel or debugging: "John Doe ➝ Augusta National"
        return f"{self.caddie.name} ➝ {self.field.name}"
    


class PlayerScore(models.Model):
    name = models.CharField(max_length=100)
    day1_score = models.IntegerField(null=True, blank=True)
    day2_score = models.IntegerField(null=True, blank=True)
    day3_score = models.IntegerField(null=True, blank=True)
    day4_score = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - Total: {self.total_score}"

    @property
    def total_score(self):
        scores = [self.day1_score, self.day2_score, self.day3_score, self.day4_score]
        return sum(score for score in scores if score is not None)
    

    