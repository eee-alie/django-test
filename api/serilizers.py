from rest_framework import serializers
from .models import ArticleModels

class Articleserializers(serializers.ModelSerializer) :
    class Meta :
        model = ArticleModels
        fields = ['title' , 'slug' , 'describtion' , 'content']
        