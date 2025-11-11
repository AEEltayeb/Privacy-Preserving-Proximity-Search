from django.db import models

# Create your models here.
class Location(models.Model):
    activity = models.CharField(max_length=100)
    x = models.FloatField()
    y = models.FloatField()

    def __str__(self):
        return f"{self.activity}: ({self.x}, {self.y})"