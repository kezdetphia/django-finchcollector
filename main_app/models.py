from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Finch(models.Model):
    name = models.CharField(max_length = 25)
    color = models.CharField(max_length = 25 )
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'{self.name}' ({self.id})


    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})