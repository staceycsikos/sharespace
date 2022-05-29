from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

  user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
  image = models.CharField(max_length=500, null=True)
  email = models.CharField(max_length=500, null=True)
  about = models.TextField(max_length=500, blank=True)
  location = models.CharField(max_length=128, blank=True)
  birthday = models.DateField(null=True, blank=True)
  hobbies = models.TextField(max_length=500, blank=True)
  profession = models.CharField(max_length=128, blank=True)
  socialmedia = models.URLField(max_length=500, blank=True, unique=True )  

  def __str__(self):
    return self.user.username