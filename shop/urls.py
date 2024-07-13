from rest_framework import routers

from shop.views import ShopViewSet

router = routers.SimpleRouter()
router.register(r'shop', ShopViewSet, basename='shop')
urlpatterns = router.urls
