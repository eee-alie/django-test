from rest_framework import routers
from .views import ArticleView


router = routers.SimpleRouter()
router.register(r'article' , ArticleView)
urlpatterns = router.urls