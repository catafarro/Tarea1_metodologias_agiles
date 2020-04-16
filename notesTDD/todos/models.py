from django.db import models

# Create your models here.

class Todo(models.Model):

    name = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    checked = models.BooleanField(default=False)
