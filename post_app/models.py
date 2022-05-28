from django.db import models
from django.forms import DateTimeField
from profile_app.models import Profile
from django.utils import timezone
## so we can have a one to many relationship
##followed projects/models.py
## related_name's must be unique, giving the same name to all the related_name's will result in errrrrr.


class Post(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_profile')
  post = models.TextField(max_length=500)
  publish_date = models.DateTimeField(default=timezone.now, blank=True)