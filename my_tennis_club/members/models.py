from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.IntegerField(null =True, blank=True)
    joined_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    