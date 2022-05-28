from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

## i do think it's weird we're not using .models in our profile views
## there's a lot more in the linkedfin views, also we weren't using
## permissions so I deleted it. 
