from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  about = models.TextField(max_length=500, blank=True)
  location = models.CharField(max_length=30, blank=True)
  birthday = models.DateField(null=True, blank=True)
  hobbies = models.TextField(max_length=500, blank=True)
  profession = models.CharField(max_length=30, blank=True)
  sociallink = models.URLField(max_length=200, unique=True, blank=True)
  
  def __str__(self):
    return self.user.username

