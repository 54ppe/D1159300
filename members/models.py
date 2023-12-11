from django.db import models

# Create your models here.
class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  age = models.IntegerField(null=True)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname} {self.age} {self.phone} {self.joined_date} " 

class Court(models.Model): 
    name = models.CharField(max_length=255)
    floor = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.name} {self.floor} {self.city}"