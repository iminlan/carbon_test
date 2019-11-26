from django.db import models


# Create your models here.
class Message(models.Model):
    name = models.DecimalField("message", max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.name)