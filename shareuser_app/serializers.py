from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = "__all__"

# we might have to change the fields?