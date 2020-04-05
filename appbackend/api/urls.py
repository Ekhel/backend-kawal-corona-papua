from .views import PenderitaViewSet, KabupatenViewSet, RsViewSet, InfoViewSet, PapanInfoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'kabupaten', KabupatenViewSet, basename='kabupaten')
router.register(r'penderita', PenderitaViewSet, basename='penderita')
router.register(r'rumahsakit', RsViewSet, basename='rumahsakit')
router.register(r'informasi', InfoViewSet, basename='informasih')
router.register(r'papaninfo', PapanInfoViewSet, basename='papaninfo')

urlpatterns = router.urls