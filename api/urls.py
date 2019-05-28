from rest_framework import routers
from .api import DishViewSet

router = routers.DefaultRouter()
router.register('api/dishes', DishViewSet,'dishes')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = router.urls