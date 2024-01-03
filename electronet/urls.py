from rest_framework.routers import DefaultRouter

from electronet.apps import ElectronetConfig

from electronet.views import FactoryViewSet, DistributorViewSet, BusinessmanViewSet, ProductViewSet

app_name = ElectronetConfig.name

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'', FactoryViewSet, basename='factory')
router.register(r'distributor', DistributorViewSet, basename='distributor')
router.register(r'businessman', BusinessmanViewSet, basename='businessman')


urlpatterns = router.urls
