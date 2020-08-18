from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.
class Diary(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to = 'photo/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return "text: " + self.text
