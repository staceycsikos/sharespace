from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)

urlpatterns = [
  path('', include(router.urls)),
]