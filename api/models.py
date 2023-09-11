from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(verbose_name="person name", max_length=50)

    def __str__(self):
        return f"{self.name}"