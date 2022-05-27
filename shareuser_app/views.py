from rest_framework import viewsets, permissions
from .serializers import ProfileSerializer
from .models import Profile

class ProfileViewSet(viewsets.ModelViewSet):
  queryset = Profile.objects.all().order_by('-date_joined')
  serializer_class = ProfileSerializer

