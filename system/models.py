from django.db import models

# Create your models here.

class TeamModel(models.Model):
    name = models.TextField(max_length=100)
    abbr = models.TextField(max_length=3)
   

    def __str__(self):
        return str(self.name)

