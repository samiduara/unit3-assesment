from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse

# Create your models here.

class lists(models.Model):
  description = models.TextField(max_length=300)
  
  def get_absolute_url(self):
        return reverse('index') 
    
  def __str__(self):
        return self.description