from django.db import models
from django.utils import timezone

# Create your models here.

class Finch(models.Model):
    name = models.CharField(max_length = 25)
    color = models.CharField(max_length = 25 )
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name