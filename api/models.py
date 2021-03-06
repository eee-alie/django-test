from django.db import models

class ArticleModels(models.Model) :
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    describtion = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.title
