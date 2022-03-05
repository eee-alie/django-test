from rest_framework import viewsets
from .serilizers import Articleserializers
from .models import ArticleModels

class ArticleView(viewsets.ModelViewSet) :
    queryset = ArticleModels.objects.all()
    serializer_class = Articleserializers
    lookup_field = "slug"