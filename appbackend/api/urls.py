from .views import PenderitaViewSet, KabupatenViewSet, RsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'kabupaten', KabupatenViewSet, basename='kabupaten')
router.register(r'penderita', PenderitaViewSet, basename='penderita')
router.register(r'rumahsakit', RsViewSet, basename='rumahsakit')


urlpatterns = router.urls