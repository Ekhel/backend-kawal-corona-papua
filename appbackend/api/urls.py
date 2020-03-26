from .views import PenderitaViewSet, KabupatenViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'kabupaten', KabupatenViewSet, basename='kabupaten')
router.register(r'penderita', PenderitaViewSet, basename='penderita')


urlpatterns = router.urls